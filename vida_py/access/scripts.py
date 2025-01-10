from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_script


def delete_work_list(session: Session) -> List[Row]:
    return run_script(session, "deleteWorkList").all()


def get_overridden_vin_component(session: Session, vin: str) -> List[Row]:
    return run_script(session, "getOverriddenVINComponent", vin=vin).all()


def usp_purge_clientlogs_table(session: Session) -> List[Row]:
    return run_script(session, "usp_purge_clientlogs_table").all()
