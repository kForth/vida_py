"""SQL function wrapper helpers for the session VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from datetime import datetime

from sqlalchemy.orm import Session

from vida_py.util import require_scalar, run_func, run_func_scalar


def get_order_date(session: Session, vehicle_id: int) -> datetime:
    value = require_scalar(run_func_scalar(session, "GetOrderDate", vehicle_id), "GetOrderDate")
    if isinstance(value, datetime):
        return value
    return datetime.fromisoformat(str(value))


def get_status(session: Session, vehicle_id: int) -> str:
    value = require_scalar(run_func_scalar(session, "GetStatus", vehicle_id), "GetStatus")
    return str(value)


def get_transaction_nbr(session: Session, vehicle_id: int) -> int:
    value = require_scalar(
        run_func_scalar(session, "GetTransactionNbr", vehicle_id),
        "GetTransactionNbr",
    )
    return int(str(value))


def split(session: Session, string: str, delimiter: str) -> list[str]:
    return [str(e) for e in run_func(session, "Split", string, delimiter).all()]
