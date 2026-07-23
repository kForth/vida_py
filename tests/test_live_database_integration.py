"""Live integration tests against configured VIDA databases."""

# ruff: noqa: PLC0415

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

import importlib
import os
import sys
from collections.abc import Generator
from contextlib import contextmanager
from typing import Any

import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

pytestmark = pytest.mark.integration

MODULE_ENV_VARS = {
    "vida_py.access": "VIDA_ACCESS_DB_URI",
    "vida_py.basedata": "VIDA_BASEDATA_DB_URI",
    "vida_py.carcom": "VIDA_CARCOM_DB_URI",
    "vida_py.diag": "VIDA_DIAG_DB_URI",
    "vida_py.epc": "VIDA_EPC_DB_URI",
    "vida_py.images": "VIDA_IMAGES_DB_URI",
    "vida_py.service": "VIDA_SERVICE_DB_URI",
    "vida_py.session": "VIDA_SESSION_DB_URI",
    "vida_py.timing": "VIDA_TIMING_DB_URI",
}

TABLE_CONTRACTS = {
    "vida_py.access": "InstalledPublication",
    "vida_py.basedata": "VehicleProfile",
    "vida_py.carcom": "T100_EcuVariant",
    "vida_py.diag": "ECU",
    "vida_py.epc": "PartItems",
    "vida_py.images": "Graphics",
    "vida_py.service": "Document",
    "vida_py.session": "HistoryItem",
    "vida_py.timing": "Requests",
}

VIEW_CONTRACTS = {
    "vida_py.basedata": "VehicleProfileDescriptions",
    "vida_py.diag": "ProfileDescription",
    "vida_py.timing": "RequestTimingView",
}

ROUTINE_CONTRACTS = {
    "vida_py.access": ("deleteWorkList", "PROCEDURE"),
    "vida_py.basedata": ("getProfileNavTitle", "FUNCTION"),
    "vida_py.carcom": ("GetText", "FUNCTION"),
    "vida_py.diag": ("GetTextFromLang", "FUNCTION"),
    "vida_py.service": ("fn_Split", "FUNCTION"),
    "vida_py.session": ("Split", "FUNCTION"),
}


def _require_db_uri_or_skip(module_name: str, env_var: str) -> str:
    value = os.getenv(env_var)
    if not value:
        pytest.skip(f"{env_var} is not configured for live integration tests ({module_name}).")
    return value


def _import_fresh(module_name: str) -> Any:
    sys.modules.pop(module_name, None)
    return importlib.import_module(module_name)


@contextmanager
def _session_for_module(module_name: str, env_var: str) -> Generator[Session]:
    _require_db_uri_or_skip(module_name, env_var)
    module = _import_fresh(module_name)
    session = module.create_session()
    try:
        yield session
    finally:
        session.close()


@pytest.mark.parametrize(("module_name", "env_var"), MODULE_ENV_VARS.items())
def test_live_database_sessions_can_execute_queries(module_name: str, env_var: str) -> None:
    with _session_for_module(module_name, env_var) as session:
        value = session.execute(text("SELECT 1")).scalar_one()

    assert value == 1


@pytest.mark.parametrize(("module_name", "table_name"), TABLE_CONTRACTS.items())
def test_live_database_contains_expected_tables(module_name: str, table_name: str) -> None:
    env_var = MODULE_ENV_VARS[module_name]

    with _session_for_module(module_name, env_var) as session:
        count = session.execute(
            text(
                "SELECT COUNT(*) "
                "FROM INFORMATION_SCHEMA.TABLES "
                "WHERE TABLE_SCHEMA = 'dbo' "
                "AND TABLE_NAME = :name "
                "AND TABLE_TYPE = 'BASE TABLE'"
            ),
            {"name": table_name},
        ).scalar_one()

    assert int(count) >= 1


@pytest.mark.parametrize(("module_name", "view_name"), VIEW_CONTRACTS.items())
def test_live_database_contains_expected_views(module_name: str, view_name: str) -> None:
    env_var = MODULE_ENV_VARS[module_name]

    with _session_for_module(module_name, env_var) as session:
        count = session.execute(
            text(
                "SELECT COUNT(*) "
                "FROM INFORMATION_SCHEMA.TABLES "
                "WHERE TABLE_SCHEMA = 'dbo' "
                "AND TABLE_NAME = :name "
                "AND TABLE_TYPE = 'VIEW'"
            ),
            {"name": view_name},
        ).scalar_one()

    assert int(count) >= 1


@pytest.mark.parametrize(("module_name", "contract"), ROUTINE_CONTRACTS.items())
def test_live_database_contains_expected_routines(
    module_name: str, contract: tuple[str, str]
) -> None:
    env_var = MODULE_ENV_VARS[module_name]
    routine_name, routine_type = contract

    with _session_for_module(module_name, env_var) as session:
        count = session.execute(
            text(
                "SELECT COUNT(*) "
                "FROM INFORMATION_SCHEMA.ROUTINES "
                "WHERE ROUTINE_SCHEMA = 'dbo' "
                "AND ROUTINE_NAME = :name "
                "AND ROUTINE_TYPE = :routine_type"
            ),
            {"name": routine_name, "routine_type": routine_type},
        ).scalar_one()

    assert int(count) >= 1


def test_live_session_split_wrapper_executes() -> None:
    from vida_py.session import funcs

    module_name = "vida_py.session"
    env_var = MODULE_ENV_VARS[module_name]

    with _session_for_module(module_name, env_var) as session:
        result = funcs.split(session, "alpha,beta", ",")

    assert isinstance(result, list)


def test_live_diag_split_wrapper_executes() -> None:
    from vida_py.diag import funcs

    module_name = "vida_py.diag"
    env_var = MODULE_ENV_VARS[module_name]

    with _session_for_module(module_name, env_var) as session:
        result = funcs.split(session, "alpha,beta", ",")

    assert isinstance(result, list)


def test_live_service_fn_split_wrapper_executes() -> None:
    from vida_py.service import funcs

    module_name = "vida_py.service"
    env_var = MODULE_ENV_VARS[module_name]

    with _session_for_module(module_name, env_var) as session:
        result = funcs.fn__split(session, "alpha,beta", ",")

    assert isinstance(result, list)
