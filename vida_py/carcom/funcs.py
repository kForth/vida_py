"""SQL function wrapper helpers for the carcom VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import require_scalar, run_func, run_func_scalar


def get_compatible_profiles(session: Session, profile: str) -> list[Row]:
    return list(run_func(session, "GetCompatibleProfiles", profile).all())


def get_dtc_code_for_customer_symptom(
    session: Session, fk_t100_ecu_variant: int, customer_symptom_id: int
) -> str:
    value = require_scalar(
        run_func_scalar(
            session, "GetDTCCodeForCustomerSymptom", fk_t100_ecu_variant, customer_symptom_id
        ),
        "GetDTCCodeForCustomerSymptom",
    )
    return str(value)


def get_text(session: Session, text_id: int) -> str:
    value = require_scalar(run_func_scalar(session, "GetText", text_id), "GetText")
    return str(value)


def get_text_from_lang(session: Session, text_id: int, language_code: str) -> str:
    value = require_scalar(
        run_func_scalar(session, "GetTextFromLang", text_id, language_code),
        "GetTextFromLang",
    )
    return str(value)


def split_big_numbers(session: Session, list_: str, delimiter: str) -> list[Row]:
    return list(run_func(session, "SplitBigNumbers", list_, delimiter).all())


def split_string(session: Session, string: str) -> list[Row]:
    return list(run_func(session, "SplitString", string).all())
