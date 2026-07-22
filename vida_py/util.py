"""Shared SQL execution helpers and configuration validation for VIDA databases."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

import os
from typing import Any

from sqlalchemy import Result, text
from sqlalchemy.engine.url import make_url
from sqlalchemy.orm import Session


def get_required_db_uri(variable_name: str) -> str:
    value = os.getenv(variable_name)
    if not value:
        raise RuntimeError(
            f"Missing required VIDA database URI environment variable: {variable_name}"
        )

    try:
        make_url(value)
    except Exception as exc:
        raise ValueError(
            f"Invalid SQLAlchemy database URI in environment variable {variable_name}: {value!r}"
        ) from exc

    return value


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
