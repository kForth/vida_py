from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.scripts import runScript


def delete_work_list(session: Session) -> List[Row]:
    return runScript(session, "deleteWorkList").all()


def get_overridden_vin_component(session: Session, vin: str) -> List[Row]:
    return runScript(session, "getOverriddenVINComponent", vin=vin).all()


def usp_purge_clientlogs_table(session: Session) -> List[Row]:
    return runScript(session, "usp_purge_clientlogs_table").all()
