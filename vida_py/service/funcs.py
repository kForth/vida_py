"""SQL function wrapper helpers for the service VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_func


def fn__split(session: Session, s_text: str, s_delim: str) -> list[Row]:
    return list(run_func(session, "fn_Split", s_text, s_delim).all())


def get_search_hits(
    session: Session, data: str, selected_profiles: str, qualifier_group: str, all_: bool
) -> list[Row]:
    return list(
        run_func(session, "getSearchHits", data, selected_profiles, qualifier_group, all_).all()
    )


def get_search_string_matches(session: Session, data: str, all_: bool) -> list[Row]:
    return list(run_func(session, "getSearchStringMatches", data, all_).all())


def hex_to_int(session: Session, vs_data: str) -> int:
    return int(str(run_func(session, "HexToInt", vs_data).all()))


def parse_search_string(session: Session, data: str) -> list[Row]:
    return list(run_func(session, "ParseSearchString", data).all())
