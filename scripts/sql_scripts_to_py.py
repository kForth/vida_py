import re

import click


def _d(d):
    if d in ("nvarchar", "varchar", "char", "nchar", "ntext", "text"):
        return "str"
    if d == "bit":
        return "bool"
    if d in ("tinyint", "bigint"):
        return "int"
    if d in ("decimal", "double", "float"):
        return "float"
    if d == "image":
        return "bytes"
    return d


def _s(s):
    s = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s).lower()


RE_CREATE_PROCEDURE = re.compile(
    r"(?:CREATE|create)\s+(?:PROCEDURE|procedure)\s+\[dbo\]\.\[([\w\d_]+)\]"
)
RE_PARAMS_DEF = re.compile(r"@(\w+)\s+(?:as\s+)?(\w+)(?:\(\d+\))?")
RE_END_DEF = re.compile(r"(^|\s+)AS(\s+|$)")


@click.command()
@click.argument("srcfiles", type=click.Path(exists=True, dir_okay=False), nargs=-1)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(srcfiles, outfile):
    funcs = []
    for fp in srcfiles:
        with open(fp, encoding="utf-16 le") as src:
            lines = src.readlines()
        name = False
        params = []
        for line in (e.strip() for e in lines):
            if not line or re.match(r"^\s*--", line):
                continue

            if m := RE_CREATE_PROCEDURE.search(line):
                name = m.group(1)
            if name and (m := RE_PARAMS_DEF.search(line)):
                params.append(m.groups())
            if RE_END_DEF.search(line):
                break
        funcs.append((name, params))

    if outfile:
        _file = open(outfile, "w+", encoding="utf-8")
        _file.writelines(
            "\n".join(
                [
                    "from datetime import datetime",
                    "from typing import List",
                    "",
                    "from sqlalchemy import Row",
                    "from sqlalchemy.orm import Session",
                    "",
                    "from PyVIDA.scripts import runScript",
                    "",
                ]
            )
        )

    _write = _file.write if outfile else click.echo
    for name, params in funcs:
        args1 = "".join(f", {_s(p)}: {_d(d)}" for p, d in params)
        args2 = "".join(f", {p}={_s(p)}" for p, _ in params)
        _write(
            "\n".join(
                [
                    "",
                    f"def {_s(name)}(session: Session{args1}) -> List[Row]:",
                    f'    return runScript(session, "{name}"{args2}).all()',
                    "",
                ]
            )
        )

    if outfile:
        _file.close()


if __name__ == "__main__":
    main()
