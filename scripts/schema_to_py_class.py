import csv

import click

FILE_HEADER = """
from datetime import datetime
from typing import List

from sqlalchemy import (
    BINARY,
    DECIMAL,
    Numeric,
    NVARCHAR,
    BigInteger,
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    SmallInteger,
    String,
    VARBINARY,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vida_py.models import Model

"""


def db_to_py_type(d):
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
    return d


def db_to_sql_type(d, s=None):
    if (d := d.lower()) in (
        "nvarchar",
        "varchar",
        "char",
        "nchar",
        "ntext",
        "text",
        "uniqueidentifier",
    ):
        return "String" + (f"({s})" if s is not None and "null" not in s.lower() else "")
    if d == "bit":
        return "Boolean"
    if d in ("tinyint", "smallint"):
        return "SmallInteger"
    if d == "bigint":
        return "BigInteger"
    if d == "int":
        return "Integer"
    if d == "decimal":
        return "DECIMAL"
    if d in ("numeric", "money", "smallmoney"):
        return "Numeric"
    if d in ("datetime", "smalldatetime"):
        return "DateTime"
    if d in ("image", "binary"):
        return "BINARY" + (f"({s})" if s is not None else "")
    if d == "varbinary":
        return "VARBINARY"
    return d


@click.command()
@click.argument("schemafile", type=click.Path(exists=True, dir_okay=False))
@click.argument("db", type=click.STRING)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(schemafile, db, outfile):
    try:
        _write = click.echo
        if outfile:
            _file = open(outfile, "w+", encoding="utf-8")

            def writeline(s: str):
                _file.write(f"{s}\n")

            _write = writeline
            _write(FILE_HEADER)

        with open(schemafile, "r", encoding="utf-8") as csvfile:

            reader = csv.reader(csvfile)
            _ = next(reader)  # skip header row

            classes = []
            last_class = None
            class_str = ""
            for line in reader:
                _class = line[2]
                if _class != last_class:
                    if last_class is not None:
                        classes.append((last_class, class_str))
                        class_str = ""
                    class_str += "\n"
                    class_str += f"class {_class}(Model):\n"
                    class_str += f'    __bind_key__ = "{db}"\n'
                    class_str += f'    __tablename__ = "{_class}"\n'
                    class_str += "\n"
                else:
                    _name = line[3]
                    _type = line[7]
                    _size = line[8]
                    _def = (
                        f", default={line[5][1:-1]}"
                        if "null" not in line[5].lower()
                        else ""
                    )
                    py_type = db_to_py_type(_type)
                    sql_type = db_to_sql_type(_type, _size) + _def
                    class_str += (
                        f"    {_name}: Mapped[{py_type}] = mapped_column({sql_type})\n"
                    )
                last_class = _class

            for _, class_str in sorted(classes, key=lambda x: x[0]):
                _write(class_str)
    finally:
        if outfile:
            _file.close()


if __name__ == "__main__":
    main()
