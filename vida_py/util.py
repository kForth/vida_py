"""Shared SQL execution helpers for invoking VIDA stored procedures and functions."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from typing import Any

from sqlalchemy import Result, text
from sqlalchemy.orm import Session


def run_script(session: Session, script: str, **kwargs: Any) -> Result:
    return session.execute(
        text(
            "\n".join(
                [
                    "DECLARE @RC int",
                    f"EXECUTE @RC = [dbo].[{script}]",
                    "\n,".join(f"@{k} = :{k}" for k in kwargs),
                    "SELECT @RC",
                ]
            )
        ),
        kwargs,
    )


def run_func(session: Session, script: str, *args: Any) -> Result:
    kwargs = {str(i): e for i, e in enumerate(args)}
    return session.execute(
        text(
            "\n".join(
                [
                    f"SELECT * FROM [dbo].[{script}] (",
                    "\n,".join(f":{k}" for k in kwargs),
                    ")",
                ]
            )
        ),
        kwargs,
    )


def run_func_scalar(session: Session, script: str, *args: Any) -> Any | None:
    return run_func(session, script, *args).scalar_one_or_none()


def require_scalar[T](value: T | None, function_name: str) -> T:
    if value is None:
        raise ValueError(f"{function_name} returned no rows")
    return value
