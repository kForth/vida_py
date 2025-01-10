import datetime
from typing import List

from sqlalchemy.orm import Session

from vida_py.util import run_func


def get_order_date(session: Session, vehicle_id: int) -> datetime:
    return run_func(session, "GetOrderDate", vehicle_id).all()


def get_status(session: Session, vehicle_id: int) -> str:
    return run_func(session, "GetStatus", vehicle_id).all()


def get_transaction_nbr(session: Session, vehicle_id: int) -> int:
    return run_func(session, "GetTransactionNbr", vehicle_id).all()


def split(session: Session, string: str, delimiter: str) -> List[str]:
    return run_func(session, "Split", string, delimiter).all()
