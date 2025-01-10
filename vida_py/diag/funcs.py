from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.funcs import run_func


def get_profile_nav_title(session: Session, fk_profile: str) -> str:
    return run_func(session, "getProfileNavTitle", fk_profile).all()


def get_sw_product_note(session: Session, sw_product_id: int) -> str:
    return run_func(session, "getSwProductNote", sw_product_id).all()


def get_text_from_lang(session: Session, text_id: int, language_code: str) -> str:
    return run_func(session, "GetTextFromLang", text_id, language_code).all()


def get_valid_profiles_for_selected(
    session: Session, selected_profiles: str
) -> List[Row]:
    return run_func(session, "GetValidProfilesForSelected", selected_profiles).all()


def split(session: Session, string: str, delimiter: str) -> List[Row]:
    return run_func(session, "Split", string, delimiter).all()


def split_big_numbers(session: Session, list: str, delimiter: str) -> List[Row]:
    return run_func(session, "SplitBigNumbers", list, delimiter).all()
