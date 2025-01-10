from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_script


def calculate_siblings(session: Session) -> List[Row]:
    return run_script(session, "calculateSiblings").all()


def clean_up(session: Session, dest_database: str) -> List[Row]:
    return run_script(session, "CleanUp", DestDatabase=dest_database).all()
