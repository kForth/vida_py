from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.funcs import run_func


def fn__split(session: Session, s_text: str, s_delim: str) -> List[Row]:
    return run_func(session, "fn_Split", s_text, s_delim).all()


def get_search_hits(
    session: Session, data: str, selected_profiles: str, qualifier_group: str, all: bool
) -> List[Row]:
    return run_func(
        session, "getSearchHits", data, selected_profiles, qualifier_group, all
    ).all()


def get_search_string_matches(session: Session, data: str, all: bool) -> List[Row]:
    return run_func(session, "getSearchStringMatches", data, all).all()


def hex_to_int(session: Session, vs_data: str) -> int:
    return run_func(session, "HexToInt", vs_data).all()


def parse_search_string(session: Session, data: str) -> List[Row]:
    return run_func(session, "ParseSearchString", data).all()
