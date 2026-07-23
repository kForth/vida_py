"""Stored procedure wrapper functions for the epc VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_script


def clean_up(session: Session) -> list[Row]:
    return list(run_script(session, "CleanUp").all())


def free_text_search(session: Session) -> list[Row]:
    return list(run_script(session, "FreeTextSearch").all())


def free_text_search_sp_generator(session: Session) -> list[Row]:
    return list(run_script(session, "FreeTextSearchSPGenerator").all())


def generate_all(session: Session) -> list[Row]:
    return list(run_script(session, "GenerateAll").all())


def get_parts_descriptions_xml(session: Session) -> list[Row]:
    return list(run_script(session, "GetPartsDescriptionsXML").all())


def insert_search_note_and_word_strings(session: Session) -> list[Row]:
    return list(run_script(session, "InsertSearchNoteAndWordStrings").all())


def parse_lexicon_fts(session: Session) -> list[Row]:
    return list(run_script(session, "ParseLexiconFTS").all())


def parse_lexicon_fts_with_delete(session: Session) -> list[Row]:
    return list(run_script(session, "ParseLexiconFTSWithDelete").all())


def restrict_usage(session: Session) -> list[Row]:
    return list(run_script(session, "RestrictUsage").all())


def set_normal_usage(session: Session) -> list[Row]:
    return list(run_script(session, "SetNormalUsage").all())


def update_lexicon(session: Session) -> list[Row]:
    return list(run_script(session, "UpdateLexicon").all())


STORED_PROCEDURES = {
    "CleanUp": clean_up,
    "FreeTextSearch": free_text_search,
    "FreeTextSearchSPGenerator": free_text_search_sp_generator,
    "GenerateAll": generate_all,
    "GetPartsDescriptionsXML": get_parts_descriptions_xml,
    "InsertSearchNoteAndWordStrings": insert_search_note_and_word_strings,
    "ParseLexiconFTS": parse_lexicon_fts,
    "ParseLexiconFTSWithDelete": parse_lexicon_fts_with_delete,
    "RestrictUsage": restrict_usage,
    "SetNormalUsage": set_normal_usage,
    "UpdateLexicon": update_lexicon,
}
