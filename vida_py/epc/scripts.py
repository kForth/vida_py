"""Stored procedure wrapper functions for the epc VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_script


def clean_up(session: Session, dest_db: str) -> list[Row]:
    return list(run_script(session, "CleanUp", DestDatabase=dest_db).all())


def free_text_search(
    session: Session,
    by: str,
    search_str: str,
    item_number: str,
    tokens: int,
    lang: int,
    notes: str,
    notes_tokens: int,
    filter_: str,
    all_: bool,
    partner_group: str,
) -> list[Row]:
    return list(
        run_script(
            session,
            "FreeTextSearch",
            By=by,
            SearchString=search_str,
            ItemNumber=item_number,
            tokens=tokens,
            lang=lang,
            notes=notes,
            notesTokens=notes_tokens,
            filter=filter_,
            all=all_,
            PartnerGroup=partner_group,
        ).all()
    )


def free_text_search_sp_generator(
    session: Session,
    by: str,
    search_str: str,
    item_number: str,
    tokens: int,
    lang: int,
    notes: str,
    notes_tokens: int,
    filter_: str,
    all_: bool,
    partner_group: str,
) -> list[Row]:
    return list(
        run_script(
            session,
            "FreeTextSearchSPGenerator",
            By=by,
            SearchString=search_str,
            ItemNumber=item_number,
            tokens=tokens,
            lang=lang,
            notes=notes,
            notesTokens=notes_tokens,
            filter=filter_,
            all=all_,
            PartnerGroup=partner_group,
        ).all()
    )


def generate_all(session: Session) -> list[Row]:
    return list(run_script(session, "GenerateAll").all())


def get_parts_descriptions_xml(session: Session, lang: int) -> list[Row]:
    return list(run_script(session, "GetPartsDescriptionsXML", lang=lang).all())


def insert_search_note_and_word_strings(
    session: Session, bulk_script_path: str, database_table: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "InsertSearchNoteAndWordStrings",
            bulkScriptPath=bulk_script_path,
            databaseTable=database_table,
        ).all()
    )


def parse_lexicon_fts(
    session: Session, description_id: int, language: int, description: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "ParseLexiconFTS",
            DescriptionId=description_id,
            fkLanguage=language,
            Description=description,
        ).all()
    )


def parse_lexicon_fts_with_delete(
    session: Session, description_id: int, language: int, description: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "ParseLexiconFTSWithDelete",
            DescriptionId=description_id,
            fkLanguage=language,
            Description=description,
        ).all()
    )


def restrict_usage(session: Session, dest_db: str) -> list[Row]:
    return list(run_script(session, "RestrictUsage", DestDatabase=dest_db).all())


def set_normal_usage(session: Session, dest_db: str) -> list[Row]:
    return list(run_script(session, "SetNormalUsage", DestDatabase=dest_db).all())


def update_lexicon(session: Session, fallback_language_id: int) -> list[Row]:
    return list(run_script(session, "UpdateLexicon", fallbacklanguageid=fallback_language_id).all())


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
