"""Stored procedure wrapper functions for the access VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_script


def delete_work_list(session: Session) -> list[Row]:
    return list(run_script(session, "deleteWorkList").all())


def get_overridden_vin_component(session: Session, vin: str, user_id: str) -> list[Row]:
    return list(run_script(session, "getOverriddenVINComponent", vin=vin, userId=user_id).all())


def usp_purge_clientlogs_table(session: Session) -> list[Row]:
    return list(run_script(session, "usp_purge_clientlogs_table").all())


STORED_PROCEDURES = {
    "deleteWorkList": delete_work_list,
    "getOverriddenVINComponent": get_overridden_vin_component,
    "usp_purge_clientlogs_table": usp_purge_clientlogs_table,
}
