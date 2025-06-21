import asyncio
import enum
import dataclasses
import hashlib
import json
import pathlib
import typing
import urllib.parse

import bs4
import aiohttp

script_dir = pathlib.Path(__file__).parent.resolve()
cache_dir = script_dir / ".cache"
utf8 = "utf8"

class TypeKind(enum.IntEnum):
    void = enum.auto()
    bool = enum.auto()
    char = enum.auto()
    short = enum.auto()
    int = enum.auto()
    uint8 = enum.auto()
    uint16 = enum.auto()
    uint32 = enum.auto()
    uint64 = enum.auto()
    int8 = enum.auto()
    int16 = enum.auto()
    int32 = enum.auto()
    int64 = enum.auto()
    long = enum.auto()
    float = enum.auto()
    double = enum.auto()
    enumc = enum.auto()
    pointer = enum.auto()
    function = enum.auto()
    array = enum.auto()
    struct = enum.auto()
    union = enum.auto()
    ident = enum.auto()
    varargs = enum.auto()

    @classmethod
    def simple_map(cls, name: str) -> typing.Optional["TypeKind"]:
        m = {
            "void": cls.void,
            "bool": cls.bool,
            "char": cls.char,
            "short": cls.short,
            "int": cls.int,
            "uint8": cls.uint8,
            "uint8_t": cls.uint8,
            "uint16": cls.uint16,
            "uint16_t": cls.uint16,
            "uint32": cls.uint32,
            "uint32_t": cls.uint32,
            "uint64": cls.uint64,
            "uint64_t": cls.uint64,
            "int8": cls.int8,
            "int8_t": cls.int8,
            "int16": cls.int16,
            "int16_t": cls.int16,
            "int32": cls.int32,
            "int32_t": cls.int32,
            "int64": cls.int64,
            "int64_t": cls.int64,
            "long": cls.long,
            "float": cls.float,
            "double": cls.double,
        }
        return m.get(name.lower())


@dataclasses.dataclass
class Type:
    kind: TypeKind = TypeKind.void
    name: str = ""
    base: typing.Optional["Type"] = None

    # TypeKind.function
    argnames: typing.List[str] = dataclasses.field(default_factory=list)
    argtypes: typing.List["Type"] = dataclasses.field(default_factory=list)
    restype: typing.Optional["Type"] = None


@dataclasses.dataclass
class Function:
    doc_url: str
    source_code: str
    name: str
    argnames: typing.List[str] = dataclasses.field(default_factory=list)
    argtypes: typing.List["Type"] = dataclasses.field(default_factory=list)
    restype: typing.Optional["Type"] = None

    def __str__(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=4)


@dataclasses.dataclass
class Item:
    key: str
    value: str


@dataclasses.dataclass
class Datatype:
    doc_url: str
    source_code: str
    name: str
    type: Type
    macros: typing.List["Item"] = dataclasses.field(default_factory=list)

    def __str__(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=4)


@dataclasses.dataclass
class Struct:
    doc_url: str
    name: str
    pass

    def __str__(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=4)


@dataclasses.dataclass
class Enumc:
    doc_url: str
    source_code: str
    name: str
    pass

    def __str__(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=4)


@dataclasses.dataclass
class Macro:
    doc_url: str
    source_code: str
    name: str
    pass

    def __str__(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=4)


@dataclasses.dataclass
class Header:
    doc_url: str
    description: str = ""
    filename: str = ""
    functions: typing.List[Function] = dataclasses.field(default_factory=list)
    datatypes: typing.List[Datatype] = dataclasses.field(default_factory=list)
    structs: typing.List[Struct] = dataclasses.field(default_factory=list)
    enums: typing.List[Enumc] = dataclasses.field(default_factory=list)
    macros: typing.List[Macro] = dataclasses.field(default_factory=list)


async def html_from_url(url: str) -> str:
    digest = hashlib.sha1(url.encode(utf8)).hexdigest()
    cache_file = cache_dir / digest
    if cache_file.exists():
        return cache_file.read_text(utf8)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            text = await response.text(utf8)
            if not text.strip():
                raise ValueError(f"Empty response for {url}")
            cache_file.write_text(text, utf8)
            return text


def comment(text: str, idx: int) -> int:
    # single line comment
    if text[idx + 1] == "/":
        idx += 2
        while text[idx] != "\n":
            idx += 1
        idx += 1  # skip newline
        return idx

    # multi line comment
    if text[idx + 1] == "*":
        idx += 2
        while text[idx : idx + 2] != "*/":
            idx += 1
        idx += 2  # skip */
    return idx


def tokenize(text: str) -> typing.List[str]:
    # 后面加空格，简化边界判断
    text = f"{text}  "
    length = len(text)
    idx = 0
    result = []
    while idx < length:
        # skip whitespace
        if text[idx].isspace():
            idx += 1
            continue

        start = idx

        # identifier
        if text[idx].isalpha() or text[idx] == "_":
            while text[idx].isalnum() or text[idx] == "_":
                idx += 1
            result.append(text[start:idx])
            continue

        #  comment
        if text[idx] == "/" and text[idx + 1] in "*/":
            idx = comment(text, idx)
            result.append(text[start:idx])
            continue

        if text[idx : idx + 3] == "...":
            idx += 3
            result.append(text[start:idx])
            continue

        # * , ( ) [ ] ; etc...
        if text[idx].isprintable():
            result.append(text[idx])
            idx += 1
            continue

        msg = f"invalid char '{text[idx]}'"
        raise ValueError(msg)

    return result


def pointer_to(base: Type) -> Type:
    return Type(TypeKind.pointer, "*", base)


def get_type(tokens: typing.List[str]) -> Type:
    idx = len(tokens) - 1
    while tokens[idx] == "const":
        idx -= 1
    ident = tokens[idx]
    if ident == "*":
        return pointer_to(get_type(tokens[:-1]))

    kind = TypeKind.simple_map(ident)
    if kind:
        return Type(kind, ident)

    return Type(TypeKind.ident, ident)


def get_type_and_name(tokens: typing.List[str]) -> typing.Tuple[Type, str]:
    name = tokens[-1]
    if name == "...":
        return Type(TypeKind.varargs, name), name
    return get_type(tokens[:-1]), name


def split_by_value(lst: typing.List[str], value: str) -> typing.List[typing.List[str]]:
    """按特定值作为分隔符分割列表"""
    result = []
    chunk = []
    for item in lst:
        if item == value:
            if chunk:  # 避免空块
                result.append(chunk)
            chunk = []
        else:
            chunk.append(item)
    if chunk:  # 添加最后一块
        result.append(chunk)
    return result


def get_arguments(
    tokens: typing.List[str],
) -> typing.Tuple[typing.List[Type], typing.List[str]]:
    if not tokens or tokens == ["void"]:
        return [], []
    argnames = []
    argtypes = []
    parts = split_by_value(tokens, ",")
    for part in parts:
        ty, name = get_type_and_name(part)
        argnames.append(name)
        argtypes.append(ty)
    return argtypes, argnames


def get_macro(text: str) -> typing.Tuple[str, str]:
    parts = text.split()
    assert parts[0] == "#define" and len(parts) >= 3, f"invalid marco definition \"{text}\""
    return parts[1], parts[2]


async def parse_function(url: str) -> Function:
    html = await html_from_url(url)

    soup = bs4.BeautifulSoup(html, "html.parser")
    tag_code = soup.select_one(".sourceCode")
    code = tag_code.text.strip()

    tokens = tokenize(code)
    lparen_idx = tokens.index("(")
    rparen_idx = tokens.index(")")
    restype, name = get_type_and_name(tokens[:lparen_idx])
    function = Function(url, code, name)
    function.restype = restype

    argtypes, argnames = get_arguments(tokens[lparen_idx+1:rparen_idx])
    function.argtypes = argtypes
    function.argnames = argnames
    return function


async def parse_datatype(url: str) -> Datatype:
    html = await html_from_url(url)

    soup = bs4.BeautifulSoup(html, "html.parser")
    tag_code = soup.select_one(".sourceCode")
    code = tag_code.text.strip()
    parts = code.splitlines()

    tokens = tokenize(parts[0])
    assert tokens[0] == "typedef", f"expected typedef but got {tokens[0]}"
    if "(" in parts[0]:
        # function def
        lparen_idx = tokens.index("(")
        rparen_idx = tokens.index(")")
        restype = get_type(tokens[1:lparen_idx])
        name = tokens[rparen_idx - 1]
        lparen_idx = tokens.index("(", rparen_idx + 1)
        rparen_idx = tokens.index(")", rparen_idx + 1)
        argtypes, argnames = get_arguments(tokens[lparen_idx + 1:rparen_idx])
        ty = Type(TypeKind.function, name, None, argnames, argtypes, restype)
    else:
        ty, name = get_type_and_name(tokens[1:-1])
    datatype = Datatype(url, code, name, ty)

    for part in parts[1:]:
        key, value = get_macro(part)
        item = Item(key, value)
        datatype.macros.append(item)

    return datatype


async def parse_header(url: str) -> Header:
    header = Header(url)
    html = await html_from_url(url)
    soup = bs4.BeautifulSoup(html, "html.parser")

    print("Functions:")
    functions_section = soup.select_one("#functions + ul")
    for tag_a in functions_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        name = tag_a.text.strip()
        try:
            function = await parse_function(def_url)
        except:
            print("error in parse_function", def_url, hashlib.sha1(def_url.encode(utf8)).hexdigest())
            raise
        print(function)
        header.functions.append(function)

    print("Datatypes:")
    datatypes_section = soup.select_one("#datatypes + ul")
    for tag_a in datatypes_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        name = tag_a.text.strip()
        print("    ", name, def_url)

    print("Structs:")
    structs_section = soup.select_one("#structs + ul")
    for tag_a in structs_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        name = tag_a.text.strip()
        print("    ", name, def_url)

    print("Enums:")
    enums_section = soup.select_one("#enums + ul")
    for tag_a in enums_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        name = tag_a.text.strip()
        print("    ", name, def_url)

    print("Macros:")
    macros_section = soup.select_one("#macros + ul")
    for tag_a in macros_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        name = tag_a.text.strip()
        print("    ", name, def_url)
    return header


async def main():
    cache_dir.mkdir(parents=True, exist_ok=True)
    doc_url = "https://wiki.libsdl.org/SDL3/APIByCategory"
    html = await html_from_url(doc_url)
    soup = bs4.BeautifulSoup(html, "html.parser")
    rows = soup.select("tbody tr")
    result = []
    for row in rows:
        tds: list = row.find_all("td")
        api_url = urllib.parse.urljoin(doc_url, tds[0].a["href"])
        description = tds[0].text
        filename = tds[1].text
        header = await parse_header(api_url)
        header.filename = filename
        header.description = description
        result.append(header)
    # print(json.dumps([dataclasses.asdict(h) for h in result], indent=4))
    await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
