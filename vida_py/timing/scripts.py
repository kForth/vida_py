"""Stored procedure wrapper functions for the timing VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_script


def get_request_timeout_and_resend(
    session: Session, ecu: int, b1: int, b2: int, b3: int
) -> list[Row]:
    return list(
        run_script(session, "GetRequestTimeoutAndResend", ECU=ecu, B1=b1, B2=b2, B3=b3).all()
    )


def get_request_timing(session: Session, ecu: int, b1: int, b2: int, b3: int) -> list[Row]:
    return list(run_script(session, "GetRequestTiming", ECU=ecu, B1=b1, B2=b2, B3=b3).all())


STORED_PROCEDURES = {
    "GetRequestTimeoutAndResend": get_request_timeout_and_resend,
    "GetRequestTiming": get_request_timing,
}
