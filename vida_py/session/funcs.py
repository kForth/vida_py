"""SQL function wrapper helpers for the session VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from datetime import datetime

from sqlalchemy.orm import Session

from vida_py.util import run_func


def get_order_date(session: Session, vehicle_id: int) -> datetime:
    return datetime.fromisoformat(str(run_func(session, "GetOrderDate", vehicle_id).all()))


def get_status(session: Session, vehicle_id: int) -> str:
    return str(run_func(session, "GetStatus", vehicle_id).all())


def get_transaction_nbr(session: Session, vehicle_id: int) -> int:
    return int(str(run_func(session, "GetTransactionNbr", vehicle_id).all()))


def split(session: Session, string: str, delimiter: str) -> list[str]:
    return [str(e) for e in run_func(session, "Split", string, delimiter).all()]
