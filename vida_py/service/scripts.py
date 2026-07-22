"""Stored procedure wrapper functions for the service VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_script


def calculate_siblings(session: Session) -> list[Row]:
    return list(run_script(session, "calculateSiblings").all())


def clean_up(session: Session, dest_database: str) -> list[Row]:
    return list(run_script(session, "CleanUp", DestDatabase=dest_database).all())
