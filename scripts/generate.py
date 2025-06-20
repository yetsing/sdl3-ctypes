import asyncio
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


@dataclasses.dataclass
class Function:
    pass


@dataclasses.dataclass
class Datatype:
    pass


@dataclasses.dataclass
class Struct:
    pass


@dataclasses.dataclass
class Enumc:
    pass


@dataclasses.dataclass
class Macro:
    pass


@dataclasses.dataclass
class Header:
    description: str = ""
    filename: str = ""
    functions: typing.List[Function] = dataclasses.field(default_factory=list)
    datatypes: typing.List[Datatype] = dataclasses.field(default_factory=list)
    structs: typing.List[Struct] = dataclasses.field(default_factory=list)
    enums: typing.List[Enumc] = dataclasses.field(default_factory=list)
    macros: typing.List[Macro] = dataclasses.field(default_factory=list)


async def html_from_url(url: str) -> str:
    digest = hashlib.sha1(url.encode()).hexdigest()
    cache_file = cache_dir / digest
    if cache_file.exists():
        return cache_file.read_text()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            cache_file.write_text(text)
            return text


async def parse_def():
    pass


async def parse_header(url: str) -> Header:
    header = Header()
    html = await html_from_url(url)
    soup = bs4.BeautifulSoup(html, "html.parser")
    sections = soup.select("ul")

    print("Functions:")
    functions_section = sections[0]
    for tag_a in functions_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        name = tag_a.text.strip()
        print("    ", name, def_url)

    print("Datatypes:")
    datatypes_section = sections[1]
    for tag_a in datatypes_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        name = tag_a.text.strip()
        print("    ", name, def_url)

    print("Structs:")
    structs_section = sections[2]
    for tag_a in structs_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        name = tag_a.text.strip()
        print("    ", name, def_url)

    print("Enums:")
    enums_section = sections[3]
    for tag_a in enums_section.select("a"):
        def_url = urllib.parse.urljoin(url, tag_a["href"])
        name = tag_a.text.strip()
        print("    ", name, def_url)

    print("Macros:")
    macros_section = sections[4]
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
