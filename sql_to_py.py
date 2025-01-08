import glob
import re


def _d(d):
    if d == "nvarchar":
        return "str"
    if d == "varchar":
        return "str"
    if d == "char":
        return "str"
    if d == "bit":
        return "bool"
    if d == "image":
        return "bytes"
    return d


for fp in glob.glob("sql\\carcom\\dbo.*.sql"):
    with open(fp, encoding="utf-16 le") as src:
        lines = src.readlines()
    name = False
    params = []
    for line in (e.strip() for e in lines):
        if not line:
            continue
        if create := re.search(r"CREATE\s+PROCEDURE", line):
            name = re.search(r"\[dbo\]\.\[([\w\d_]+)\]", line).group(1)
        if line.endswith("AS"):
            break
        if name and not create:
            match = re.search(r"(\w+)\s+(\w+)(?:\(\d+\))?", line)
            params.append(match.groups())
    print(
        "\n".join(
            [
                f"def {name}(session: Session{''.join(f', {p}: {_d(d)}' for p, d in params)}):",
                f"  return runScript(session, \"{name}\"{''.join(f', {p}={p}' for p, d in params)}).all()",
                "",
            ]
        )
    )
