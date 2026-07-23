"""SQL function wrapper helpers for the epc VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_func, run_func_scalar


def fn__split_with_level(session: Session, text: str, level: int) -> str:
    return run_func_scalar(session, "fn_SplitWithLevel", text, level)


def get_ns_text(session: Session, id_: int, lang: int) -> str:
    return run_func_scalar(session, "GetNSText", id_, lang)


def get_part_notes(session: Session, id_: int, lang: int) -> str:
    return run_func_scalar(session, "GetPartNotes", id_, lang)


def get_part_text(session: Session, id_: int, lang: int) -> str:
    return run_func_scalar(session, "GetPartText", id_, lang)


def get_path(session: Session, cid: int, path: str) -> str:
    return run_func_scalar(session, "getPath", cid, path)


def get_section_description(
    session: Session, section_id: int, language: int, structured_notes: str
) -> str:
    return run_func_scalar(session, "getSectionDescription", section_id, language, structured_notes)


def get_section_doc_footnote(session: Session, section_id: int, language: int) -> str:
    return run_func_scalar(session, "getSectionDocFootnote", section_id, language)


def get_section_variant_footnote(session: Session, section_id: int, language: int) -> str:
    return run_func_scalar(session, "getSectionVariantFootnote", section_id, language)


def parse_note_search_string(session: Session, data: str, language: int) -> list[Row]:
    return list(run_func(session, "ParseNoteSearchString", data, language).all())


def parse_part_search_string(session: Session, data: str, language: int) -> list[Row]:
    return list(run_func(session, "ParsePartSearchString", data, language).all())


def parse_string(session: Session, string: str) -> list[Row]:
    return list(run_func(session, "ParseString", string).all())


def parse_to_words(session: Session, data: str) -> list[Row]:
    return list(run_func(session, "ParseToWords", data).all())


FUNCTIONS = {
    "fn_SplitWithLevel": fn__split_with_level,
    "GetNSText": get_ns_text,
    "GetPartNotes": get_part_notes,
    "GetPartText": get_part_text,
    "getPath": get_path,
    "getSectionDescription": get_section_description,
    "getSectionDocFootnote": get_section_doc_footnote,
    "getSectionVariantFootnote": get_section_variant_footnote,
    "ParseNoteSearchString": parse_note_search_string,
    "ParsePartSearchString": parse_part_search_string,
    "ParseString": parse_string,
    "ParseToWords": parse_to_words,
}
