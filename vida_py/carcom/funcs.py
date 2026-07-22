"""SQL function wrapper helpers for the carcom VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_func


def get_compatible_profiles(session: Session, profile: str) -> list[Row]:
    return list(run_func(session, "GetCompatibleProfiles", profile).all())


def get_dtc_code_for_customer_symptom(
    session: Session, fk_t100_ecu_variant: int, customer_symptom_id: int
) -> str:
    return str(
        run_func(
            session, "GetDTCCodeForCustomerSymptom", fk_t100_ecu_variant, customer_symptom_id
        ).all()
    )


def get_text(session: Session, text_id: int) -> str:
    return str(run_func(session, "GetText", text_id).all())


def get_text_from_lang(session: Session, text_id: int, language_code: str) -> str:
    return str(run_func(session, "GetTextFromLang", text_id, language_code).all())


def split_big_numbers(session: Session, list_: str, delimiter: str) -> list[Row]:
    return list(run_func(session, "SplitBigNumbers", list_, delimiter).all())


def split_string(session: Session, string: str) -> list[Row]:
    return list(run_func(session, "SplitString", string).all())
