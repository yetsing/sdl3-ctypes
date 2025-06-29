import asyncio
import dataclasses
import enum
import functools
import hashlib
import json
import os
import pathlib
import platform
import shutil
import string
import subprocess
import time
import typing
import urllib.parse

import aiohttp
import bs4

script_dir = pathlib.Path(__file__).parent.resolve()
cache_dir = script_dir / ".cache"
utf8 = "utf8"
package_name = "sdl3_ctypes"

# region utils function


def debug_wrapper(func: typing.Callable) -> typing.Callable:
    @functools.wraps(func)
    def wrapper(self: typing.Any, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        try:
            return func(self, *args, **kwargs)
        except:
            print(self.source_code)
            print(self.doc_url)
            raise

    return wrapper


def comment_multline(text: str) -> str:
    lines = text.splitlines()
    return "\n".join(f"# {line}" for line in lines if line.strip())

# endregion


# region Dataclass definition

Defines = typing.Dict[str, typing.Union["Datatype", "Struct", "Enumc"]]

cfunctype_tpl = """
# {source_code}
{name} = ctypes.CFUNCTYPE({restype}, {argtypes})
"""
pycode_tpl = r"""{document}

{imports}
{body}
"""


def convert_enum_and_macro(type_s: str, name: str, defines: Defines) -> typing.Tuple[str, str]:
    """转换枚举和宏为对应的整数类型"""
    if not name:
        # simple type
        return type_s, name

    define = defines[name]
    if isinstance(define, Enumc):
        return "ctypes.c_int", ""
    if isinstance(define, Datatype) and define.type.isint():
        newtype, name2 = define.type.convert({})  # 传空防止递归
        assert name2 == "", f"invalid type: {name} {define}"
        return newtype, ""

    return type_s, name


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

    # TypeKind.array
    size: int = -1

    def isint(self):
        return self.kind in {
            TypeKind.int, TypeKind.uint8, TypeKind.uint16, TypeKind.uint32, TypeKind.uint64,
            TypeKind.int8, TypeKind.int16, TypeKind.int32, TypeKind.int64, TypeKind.long,
        }

    def convert(self, defines: Defines) -> typing.Tuple[str, str]:
        mapping = {
            TypeKind.void: "None",
            TypeKind.bool: "ctypes.c_bool",
            TypeKind.char: "ctypes.c_char",
            TypeKind.short: "ctypes.c_short",
            TypeKind.int: "ctypes.c_int",
            TypeKind.uint8: "ctypes.c_uint8",
            TypeKind.uint16: "ctypes.c_uint16",
            TypeKind.uint32: "ctypes.c_uint32",
            TypeKind.uint64: "ctypes.c_uint64",
            TypeKind.int8: "ctypes.c_int8",
            TypeKind.int16: "ctypes.c_int16",
            TypeKind.int32: "ctypes.c_int32",
            TypeKind.int64: "ctypes.c_int64",
            TypeKind.long: "ctypes.c_long",
            TypeKind.float: "ctypes.c_float",
            TypeKind.double: "ctypes.c_double",
            TypeKind.enumc: "ctypes.c_int",
            TypeKind.function: self.name,
            TypeKind.ident: self.name,
        }
        if self.kind == TypeKind.pointer:
            if self.base.kind == TypeKind.char:
                return "ctypes.c_char_p", ""
            if self.base.kind == TypeKind.void:
                return "ctypes.c_void_p", ""
            if self.base.kind == TypeKind.pointer and self.base.base.kind == TypeKind.void:
                return "ctypes.POINTER(ctypes.c_void_p)", ""
            sub, name = self.base.convert(defines)
            return f"ctypes.POINTER({sub})", name
        if (
            self.kind == TypeKind.array
            and self.base.kind == TypeKind.pointer
            and self.base.base.kind == TypeKind.char
        ):
            # char *argv[]
            return "ctypes.POINTER(ctypes.c_char_p)", ""
        name = ""
        if self.kind == TypeKind.ident:
            name = self.name
        return convert_enum_and_macro(mapping[self.kind], name, defines)


@dataclasses.dataclass
class Function:
    doc_url: str
    source_code: str
    name: str
    argnames: typing.List[str] = dataclasses.field(default_factory=list)
    argtypes: typing.List["Type"] = dataclasses.field(default_factory=list)
    restype: typing.Optional["Type"] = None
    header: str = ""

    def __str__(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=4)

    @debug_wrapper
    def convert_py(self, libname: str, defines: Defines) -> typing.Tuple[str, typing.List[str]]:
        unresolve_names = []
        argtypes_list = []
        for t in self.argtypes:
            s, name = t.convert(defines)
            if name:
                unresolve_names.append(name)
            argtypes_list.append(s)
        argtypes = ", ".join(argtypes_list)
        restype, name = self.restype.convert(defines)
        assert name == "", f"invalid restype: {restype} {name}"
        code = f"""
# {self.source_code}
{self.name} = {libname}.{self.name}
{self.name}.argtypes = [{argtypes}]
{self.name}.restype = {restype}
"""
        return code, unresolve_names


@dataclasses.dataclass
class DatatypeItem:
    key: str
    value: int


@dataclasses.dataclass
class Datatype:
    doc_url: str
    source_code: str
    name: str
    type: Type
    macros: typing.List["DatatypeItem"] = dataclasses.field(default_factory=list)
    header: str = ""

    def __str__(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=4)

    @debug_wrapper
    def convert_py(self, libname: str, defines: Defines) -> typing.Tuple[str, typing.List[str]]:
        if self.type.kind == TypeKind.function:
            unresolve_names = []
            argtypes_list = []
            for t in self.type.argtypes:
                s, name = t.convert(defines)
                argtypes_list.append(s)
                if name:
                    unresolve_names.append(name)
            argtypes = ", ".join(argtypes_list)
            restype, name = self.type.restype.convert(defines)
            assert name == "", f"invalid restype: {restype} {name}"
            code = cfunctype_tpl.format(
                source_code=self.source_code,
                name=self.name,
                restype=restype,
                argtypes=argtypes,
            )
            return code, unresolve_names
        assert self.type.isint(), f"Datatype expected int, got {self.type.kind}"
        codes = [comment_multline(self.source_code)]
        for item in self.macros:
            codes.append(f"{item.key} = {item.value}")
        return "\n".join(codes), []


@dataclasses.dataclass
class Struct:
    doc_url: str
    source_code: str
    name: str
    argnames: typing.List[str] = dataclasses.field(default_factory=list)
    argtypes: typing.List["Type"] = dataclasses.field(default_factory=list)
    header: str = ""

    def __str__(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=4)


@dataclasses.dataclass
class EnumItem:
    key: str
    value: typing.Union[int, str]


@dataclasses.dataclass
class Enumc:
    doc_url: str
    source_code: str
    name: str
    items: typing.List["EnumItem"] = dataclasses.field(default_factory=list)

    def __str__(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=4)


@dataclasses.dataclass
class Macro:
    doc_url: str
    source_code: str
    name: str
    value: typing.Union[int, str]

    def __str__(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=4)

    @classmethod
    def get_value(cls, name: str) -> int:
        """获取一些宏的值"""
        m = {
            "SDL_MESSAGEBOX_COLOR_COUNT": 5,
        }
        return m[name]


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

    def convert_py(self, libname: str, defines: Defines) -> str:
        imports = [
            "import ctypes",
            f"from {package_name}.lib import {libname}",
        ]
        codes = []
        unresolve_names = []

        for datatype in self.datatypes:
            code, names = datatype.convert_py(libname, defines)
            codes.append(code)
            unresolve_names.extend(names)

        if self.filename == "SDL_main.h":
            code, names = self.convert_func_sdl_main(libname, defines)
            codes.append(code)
            unresolve_names.extend(names)
        else:
            for func in self.functions:
                code, names = func.convert_py(libname, defines)
                codes.append(code)
                unresolve_names.extend(names)

        for name in unresolve_names:
            define = defines[name]
            if define.header == self.filename:
                continue
            module = define.header[:-2]
            imports.append(f"from {package_name}.{module} import {name}")

        document = (
            f'"""\n{self.filename}\n{self.description}\nDocument: {self.doc_url}\n"""'
        )
        imports_s = "\n".join(imports)
        code_s = "\n".join(codes)
        return pycode_tpl.format(document=document, imports=imports_s, body=code_s)

    def convert_func_sdl_main(
        self, libname: str, defines: Defines,
    ) -> typing.Tuple[str, typing.List[str]]:
        """特殊处理 SDL_main.h"""
        codes = []

        ignored = {
            "SDL_AppEvent",
            "SDL_AppInit",
            "SDL_AppIterate",
            "SDL_AppQuit",
            "SDL_main",
        }
        unresolve_names = []
        for func in self.functions:
            if func.name in ignored:
                continue
            code, names = func.convert_py(libname, defines)
            codes.append(code)
            unresolve_names.extend(names)

        return "".join(codes), unresolve_names


# endregion


# region Parse util


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

        # string
        if text[idx] == '"':
            idx += 1
            while text[idx] != '"':
                idx += 1
            idx += 1
            result.append(text[start:idx])
            continue

        # identifier
        if text[idx].isalpha() or text[idx] == "_":
            while text[idx].isalnum() or text[idx] == "_":
                idx += 1
            result.append(text[start:idx])
            continue

        # prefix: 0x 0X suffix: u lu U LU etc...
        special_digits = "xXluLu" + string.hexdigits

        # negative integer
        if text[idx] == "-" and text[idx + 1].isdigit():
            idx += 2
            while text[idx].isdigit() or text[idx] in special_digits:
                idx += 1
            result.append(text[start:idx])
            continue

        # integer
        if text[idx].isdigit():
            while text[idx].isdigit() or text[idx] in special_digits:
                idx += 1
            result.append(text[start:idx])
            continue

        #  comment
        if text[idx] == "/" and text[idx + 1] in "*/":
            idx = comment(text, idx)
            # result.append(text[start:idx])
            continue

        if text[idx : idx + 3] == "...":
            idx += 3
            result.append(text[start:idx])
            continue

        # * , ( ) [ ] ; # etc...
        if text[idx].isprintable():
            result.append(text[idx])
            idx += 1
            continue

        msg = f"invalid char '{text[idx]}'"
        raise ValueError(msg)

    return result


def pointer_to(base: Type) -> Type:
    return Type(TypeKind.pointer, "*", base)


def array_to(base: Type, size: int) -> Type:
    return Type(TypeKind.array, "[]", base, size=size)


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
    if name == "]":
        assert tokens.count("[") == 1, "invalid array"
        lbracket_idx = tokens.index("[")
        name = tokens[lbracket_idx - 1]
        base = get_type(tokens[: lbracket_idx - 1])
        size = -1
        if tokens[lbracket_idx + 1] != "]":
            if tokens[lbracket_idx + 1].isdigit():
                size = int(tokens[lbracket_idx + 1])
            else:
                size = Macro.get_value(tokens[lbracket_idx + 1])
        return array_to(base, size), name
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
    seperator: str = ",",
) -> typing.Tuple[typing.List[Type], typing.List[str]]:
    if not tokens or tokens == ["void"]:
        return [], []
    argnames = []
    argtypes = []
    parts = split_by_value(tokens, seperator)
    for part in parts:
        ty, name = get_type_and_name(part)
        argnames.append(name)
        argtypes.append(ty)
    return argtypes, argnames


def run_c_code(code: str) -> str:
    """运行 C 代码返回输出"""
    if platform.system() == "Windows":
        cc = r"C:\msys64\ucrt64\bin\gcc.exe"
        if not os.path.exists(cc):
            msg = f"Can't find '{cc}'. Please install MSYS2"
            raise ValueError(msg)
    else:
        cc = shutil.which("cc")
    filename = f"hello_{int(time.time())}.c"
    with open(filename, "w", encoding=utf8) as f:
        f.write(code)

    env = os.environ.copy()
    if platform.system() == "Windows":
        ucrt64_bin = r"C:\msys64\ucrt64\bin"
        env["PATH"] = f"{ucrt64_bin};{env['PATH']}"  # 添加 ucrt64 到 PATH
        env["MSYSTEM"] = "UCRT64"  # 设置 MSYS2 子系统
    try:
        subprocess.check_call([cc, "-o", "hello", filename], env=env)
        return subprocess.check_output(["./hello"], env=env, text=True)
    finally:
        os.unlink(filename)


def get_macros(text: str) -> typing.List[DatatypeItem]:
    if not text.strip():
        return []
    print_stmts = []
    for line in text.splitlines():
        name = line.split()[1]
        if "(" in name:
            # 跳过函数宏
            continue
        stmt = r'printf("{}=%lld\n", {});'.format(name, name)
        print_stmts.append(stmt)
    body = "\n".join(print_stmts)
    code = f"""
#include <stdio.h>
#include <stdint.h>

#define SDL_UINT64_C(c)  c ## ULL /* or whatever the current compiler uses. */
#define SDL_SINT64_C(c)  c ## LL  /* or whatever the current compiler uses. */

typedef uint8_t Uint8;
#define SDL_MAX_UINT8   ((Uint8)0xFF)           /* 255 */
#define SDL_MIN_UINT8   ((Uint8)0x00)           /* 0 */
typedef int8_t Sint8;
#define SDL_MAX_SINT8   ((Sint8)0x7F)           /* 127 */
#define SDL_MIN_SINT8   ((Sint8)(~0x7F))        /* -128 */
typedef int16_t Sint16;
#define SDL_MAX_SINT16  ((Sint16)0x7FFF)        /* 32767 */
#define SDL_MIN_SINT16  ((Sint16)(~0x7FFF))     /* -32768 */
typedef uint16_t Uint16;
#define SDL_MAX_UINT16  ((Uint16)0xFFFF)        /* 65535 */
#define SDL_MIN_UINT16  ((Uint16)0x0000)        /* 0 */
typedef uint32_t Uint32;
#define SDL_MAX_UINT32  ((Uint32)0xFFFFFFFFu)   /* 4294967295 */
#define SDL_MIN_UINT32  ((Uint32)0x00000000)    /* 0 */
typedef int32_t Sint32;
#define SDL_MAX_SINT32  ((Sint32)0x7FFFFFFF)    /* 2147483647 */
#define SDL_MIN_SINT32  ((Sint32)(~0x7FFFFFFF)) /* -2147483648 */
typedef int64_t Sint64;
#define SDL_MAX_SINT64  SDL_SINT64_C(0x7FFFFFFFFFFFFFFF)   /* 9223372036854775807 */
#define SDL_MIN_SINT64  ~SDL_SINT64_C(0x7FFFFFFFFFFFFFFF)  /* -9223372036854775808 */
typedef uint64_t Uint64;
#define SDL_MAX_UINT64  SDL_UINT64_C(0xFFFFFFFFFFFFFFFF)   /* 18446744073709551615 */
#define SDL_MIN_UINT64  SDL_UINT64_C(0x0000000000000000)   /* 0 */


{text}

int main() {{

{body}

    return 0;
}}
"""
    specials = {
        "SDL_MAX_SINT64": 9223372036854775807,
        "SDL_MIN_SINT64": -9223372036854775808,
        "SDL_MAX_UINT64": 18446744073709551615,
        "SDL_MIN_UINT64": 0,
    }
    output = run_c_code(code)
    result = []
    for line in output.splitlines():
        line = line.strip()
        if not line:
            continue
        k, v = line.split("=", 1)
        item = DatatypeItem(k, int(v))
        if k in specials:
            item.value = specials[k]
        result.append(item)
    return result


def strip_macro(code: str) -> str:
    """去除代码里面的宏"""
    result = []
    for line in code.splitlines():
        if line.strip().startswith("#"):
            continue
        result.append(line)
    return "\n".join(result)


async def get_source_code(url: str) -> str:
    html = await html_from_url(url)

    soup = bs4.BeautifulSoup(html, "html.parser")
    tag_code = soup.select_one(".sourceCode")
    return tag_code.text.strip()


# endregion


# region Parse function


async def parse_function(url: str) -> Function:
    code = await get_source_code(url)

    tokens = tokenize(code)
    lparen_idx = tokens.index("(")
    rparen_idx = tokens.index(")")
    restype, name = get_type_and_name(tokens[:lparen_idx])
    function = Function(url, code, name)
    function.restype = restype

    argtypes, argnames = get_arguments(tokens[lparen_idx + 1 : rparen_idx])
    function.argtypes = argtypes
    function.argnames = argnames
    return function


async def parse_datatype(url: str) -> Datatype:
    code = await get_source_code(url)
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
        argtypes, argnames = get_arguments(tokens[lparen_idx + 1 : rparen_idx])
        ty = Type(TypeKind.function, name, None, argnames, argtypes, restype)
    else:
        ty, name = get_type_and_name(tokens[1:-1])
    datatype = Datatype(url, code, name, ty)

    macro_code = "\n".join(
        part for part in parts[1:] if part and (not part.startswith("#endif"))
    )
    datatype.macros = get_macros(macro_code)
    return datatype


async def parse_struct(url: str) -> Struct:
    code = await get_source_code(url)

    tokens = tokenize(code)
    if tokens[0] == "typedef" and (tokens[1] == "struct" or tokens[1] == "union"):
        # typedef struct/union xxx { ... } xxx;
        name = tokens[-2]
    elif tokens[0] == "struct":
        # struct xxx { ... };
        name = tokens[1]
    else:
        raise ValueError(f"invalid struct: {code}")
    lbrace_idx = tokens.index("{")
    rbrace_idx = tokens.index("}")
    argtypes, argnames = get_arguments(tokens[lbrace_idx + 1 : rbrace_idx], ";")

    struct = Struct(url, code, name)
    struct.argtypes = argtypes
    struct.argnames = argnames
    return struct


async def parse_enum(url: str) -> Enumc:
    code = await get_source_code(url)

    # typedef enum xxx { ... } xxx;
    tokens = tokenize(code)
    assert tokens[0] == "typedef" and tokens[1] == "enum", f"invalid enum: {code}"
    name = tokens[-2]
    enumc = Enumc(url, code, name)
    if name in ("SDL_PixelFormat", "SDL_AudioFormat"):
        # SDL_PixelFormat SDL_AudioFormat
        # 存在 #if 宏，根据平台会有不同的值
        # 所以不解析，后面手动生成这个枚举
        return enumc

    lbrace_idx = tokens.index("{")
    rbrace_idx = tokens.index("}")
    # parse define enum values
    value_tokens = tokens[lbrace_idx + 1 : rbrace_idx]
    auto_value = 0
    items = []
    item_mapping = {}
    for part in split_by_value(value_tokens, ","):
        item = EnumItem("", auto_value)
        if len(part) == 1:
            key = part[0]
            item.key = key
            item.value = auto_value
            auto_value += 1
        elif len(part) == 3:
            assert part[1] == "=", f"invalid enum value: {code}"
            key = part[0]
            item.key = key
            value_s = part[2].rstrip("luLu")
            try:
                base = 10
                if value_s.startswith("0x") or value_s.startswith("0X"):
                    base = 16
                auto_value = int(value_s, base)
                item.value = auto_value
                auto_value += 1
            except ValueError:
                # xxx = xxx
                auto_value = item_mapping[part[2]]
                item.value = part[2]  # 保留原有赋值
        else:
            raise ValueError(f"invalid enum value: {part}\n{code}")

        item_mapping[item.key] = item.value
        items.append(item)

    enumc.items = items
    return enumc


async def parse_macro(url: str) -> Macro:
    code = await get_source_code(url)

    tokens = code.replace("\\\n", "").split(" ", 2)
    assert len(tokens) == 3 and tokens[0] == "#define", f"invalid macro: {code}"

    key = tokens[1].strip()
    value = tokens[2].strip()
    if value.isdigit() or value.startswith("0x"):
        value = value.rstrip("luLU")
        base = 10
        if value.startswith("0x"):
            base = 16
        value = int(value, base=base)
    macro = Macro(url, code, key, value)
    return macro


async def parse_header(url: str, description: str, filename: str) -> Header:
    header = Header(url, description, filename)
    html = await html_from_url(url)
    soup = bs4.BeautifulSoup(html, "html.parser")

    functions_section = soup.select_one("#functions + ul")
    for tag_a in functions_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        # name = tag_a.text.strip()
        function = await parse_function(def_url)
        function.header = header.filename
        header.functions.append(function)

    datatypes_section = soup.select_one("#datatypes + ul")
    for tag_a in datatypes_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        # name = tag_a.text.strip()
        datatype = await parse_datatype(def_url)
        datatype.header = header.filename
        header.datatypes.append(datatype)

    structs_section = soup.select_one("#structs + ul")
    for tag_a in structs_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        # name = tag_a.text.strip()
        struct = await parse_struct(def_url)
        struct.header = header.filename
        header.structs.append(struct)

    enums_section = soup.select_one("#enums + ul")
    for tag_a in enums_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        # name = tag_a.text.strip()
        enumc = await parse_enum(def_url)
        enumc.header = header.filename
        header.enums.append(enumc)

    macros_section = soup.select_one("#macros + ul")
    for tag_a in macros_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        # name = tag_a.text.strip()
        macro = await parse_macro(def_url)
        macro.header = header.filename
        header.macros.append(macro)

    return header


async def parse(url: str) -> typing.List[Header]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    html = await html_from_url(url)
    soup = bs4.BeautifulSoup(html, "html.parser")
    rows = soup.select("tbody tr")
    result = []
    for row in rows:
        tds: list = row.find_all("td")
        api_url = urllib.parse.urljoin(url, tds[0].a["href"])
        description = tds[0].text
        filename = tds[1].text
        header = await parse_header(api_url, description, filename)
        result.append(header)
    return result


# endregion


async def main():
    doc_url = "https://wiki.libsdl.org/SDL3/APIByCategory"
    result = await parse(doc_url)

    defines: Defines = {}
    for header in result:
        for datatype in header.datatypes:
            defines[datatype.name] = datatype
        for struct in header.structs:
            defines[struct.name] = struct
        for enumc in header.enums:
            defines[enumc.name] = enumc

    libname = "libsdl3"
    output_dir = script_dir.parent / package_name
    for header in result[:2]:
        output_filename = output_dir / (header.filename.replace(".h", ".py"))
        output_filename.write_text(header.convert_py(libname, defines))
    if not shutil.which("uvx"):
        raise RuntimeError("uvx not found")
    subprocess.check_call(["uvx", "isort", output_dir])
    subprocess.check_call(["uvx", "black", output_dir])
    await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
