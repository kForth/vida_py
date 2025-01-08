from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.scripts import runScript


def clean_up(session: Session, dest_database: str) -> List[Row]:
    return runScript(session, "CleanUp", DestDatabase=dest_database).all()
