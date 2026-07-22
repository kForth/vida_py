"""SQL function wrapper helpers for the diag VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_func, run_func_scalar


def get_profile_nav_title(session: Session, fk_profile: str) -> str:
    return run_func_scalar(session, "getProfileNavTitle", fk_profile)


def get_sw_product_note(session: Session, sw_product_id: int) -> str:
    return run_func_scalar(session, "getSwProductNote", sw_product_id)


def get_text_from_lang(session: Session, text_id: int, language_code: str) -> str:
    return run_func_scalar(session, "GetTextFromLang", text_id, language_code)


def get_valid_profiles_for_selected(session: Session, selected_profiles: str) -> list[Row]:
    return list(run_func(session, "GetValidProfilesForSelected", selected_profiles).all())


def split(session: Session, string: str, delimiter: str) -> list[Row]:
    return list(run_func(session, "Split", string, delimiter).all())


def split_big_numbers(session: Session, list_: str, delimiter: str) -> list[Row]:
    return list(run_func(session, "SplitBigNumbers", list_, delimiter).all())
