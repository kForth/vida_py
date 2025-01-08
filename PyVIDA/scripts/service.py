from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from PyVIDA.scripts import runScript


def calculate_siblings(session: Session) -> List[Row]:
    return runScript(session, "calculateSiblings").all()


def clean_up(session: Session, dest_database: str) -> List[Row]:
    return runScript(session, "CleanUp", DestDatabase=dest_database).all()
