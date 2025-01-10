import re

import click


def to_py_type(d: str) -> str:
    if (d := d.lower()) in (
        "nvarchar",
        "varchar",
        "char",
        "nchar",
        "ntext",
        "text",
        "uniqueidentifier",
    ):
        return "str"
    if d == "bit":
        return "bool"
    if d in ("tinyint", "smallint", "bigint"):
        return "int"
    if d in ("decimal", "double", "float", "numeric", "money"):
        return "float"
    if d == "image":
        return "bytes"
    if d == "smalldatetime":
        return "datetime"
    if d in ("images", "binary", "varbinary"):
        return "bytes"
    if d in ("none", "null"):
        return "None"
    if d == "table":
        return "List[Row]"
    return d


def _snake(s: str) -> str:
    s = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s).lower()


RE_CREATE_PROCEDURE = re.compile(
    r"[Cc][Rr][Ee][Aa][Tt][Ee]\s+[Ff][Uu][Nn][Cc][Tt][Ii][Oo][Nn]\s+\[dbo\]\.\[([\w\d_]+)\]"
)
RE_PARAMS_DEF = re.compile(r"@(\w+)\s+(?:as\s+)?(\w+)(?:\(\d+\))?")
RE_RETURN_DEF = re.compile(r"(?:RETURNS|returns)\s+(\w+)(?:\(\d+\))?")
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
        ret = "None"
        params = []
        for line in (e.strip() for e in lines):
            if not line or re.match(r"^\s*--", line):
                continue
            if m := RE_CREATE_PROCEDURE.search(line):
                name = m.group(1)
            if name and (m := RE_PARAMS_DEF.findall(line)):
                params += m
            if name and (m := RE_RETURN_DEF.search(line)):
                ret = m.group(1)
            if RE_END_DEF.search(line):
                break
        funcs.append((name, ret, params))

    if outfile:
        _file = open(outfile, "w+", encoding="utf-8")
        _file.writelines(
            "\n".join(
                [
                    "from sqlalchemy.orm import Session",
                    "",
                    "from vida_py.util import run_func",
                    "",
                ]
            )
        )

    _write = _file.write if outfile else click.echo
    for name, ret, params in funcs:
        args1 = "".join(f", {_snake(p)}: {to_py_type(d)}" for p, d in params)
        args2 = "".join(f", {_snake(p)}" for p, _ in params)
        _write(
            "\n".join(
                [
                    "",
                    f"def {_snake(name)}(session: Session{args1}) -> {to_py_type(ret)}:",
                    f'    return run_func(session, "{name}"{args2}).all()',
                    "",
                ]
            )
        )

    if outfile:
        _file.close()


if __name__ == "__main__":
    main()
