"""SQL function wrapper helpers for the session VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from datetime import datetime

from sqlalchemy.orm import Session

from vida_py.util import run_func, run_func_scalar


def get_order_date(session: Session, vehicle_id: int) -> datetime:
    return run_func_scalar(session, "GetOrderDate", vehicle_id)


def get_status(session: Session, vehicle_id: int) -> str:
    return run_func_scalar(session, "GetStatus", vehicle_id)


def get_transaction_nbr(session: Session, vehicle_id: int) -> int:
    return run_func_scalar(session, "GetTransactionNbr", vehicle_id)


def split(session: Session, string: str, delimiter: str) -> list[str]:
    return [str(e) for e in run_func(session, "Split", string, delimiter).all()]


FUNCTIONS = {
    "GetOrderDate": get_order_date,
    "GetStatus": get_status,
    "GetTransactionNbr": get_transaction_nbr,
    "Split": split,
}
