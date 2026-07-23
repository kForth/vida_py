"""Live integration tests for implementation coverage against VIDA databases."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

import ast
import importlib
import inspect as pyinspect
import os
import sys
from collections.abc import Generator
from contextlib import contextmanager
from typing import Any

import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

pytestmark = pytest.mark.integration

MODULES = (
    "access",
    "basedata",
    "carcom",
    "diag",
    "epc",
    "images",
    "service",
    "session",
    "timing",
)
SUBMODULES: tuple[str, ...] = ("models", "views", "funcs", "scripts")


def _discover_module_components(module_name: str) -> dict[str, str]:
    components: dict[str, str] = {}
    for suffix in SUBMODULES:
        candidate = f"vida_py.{module_name}.{suffix}"
        if importlib.util.find_spec(candidate) is not None:
            components[suffix] = candidate
    return components


MODULE_ENV_VARS = {f"vida_py.{e}": f"VIDA_{e.upper()}_DB_URI" for e in MODULES}

MODULE_COMPONENTS = {f"vida_py.{module}": _discover_module_components(module) for module in MODULES}

# These model-only key columns are intentionally not present in DB objects.
KNOWN_SYNTHETIC_COLUMNS: dict[tuple[str, str], set[str]] = {
    ("vida_py.diag.models", "EcuDescription"): {"id"},
    ("vida_py.diag.models", "IEGenericComponent"): {"id"},
    ("vida_py.diag.models", "SmartToolScript"): {"id"},
    ("vida_py.session.models", "ActionItem"): {"id"},
}

# System tables to ignore missing implementations
SYSTEM_TABLES: set[str] = {"dtproperties", "sysdiagrams"}


def _require_db_uri(module_name: str, env_var: str) -> str:
    value = os.getenv(env_var)
    assert value, f"{env_var} is not configured for live integration tests ({module_name})."
    return value


def _import_fresh(module_name: str) -> Any:
    sys.modules.pop(module_name, None)
    return importlib.import_module(module_name)


@contextmanager
def _session_for_module(module_name: str, env_var: str) -> Generator[Session]:
    _require_db_uri(module_name, env_var)
    module = _import_fresh(module_name)
    session = module.create_session()
    try:
        yield session
    finally:
        session.close()


def _normalize(names: set[str]) -> set[str]:
    return {name.strip().lower() for name in names}


def _query_names(session: Session, query: str) -> set[str]:
    rows = session.execute(text(query)).all()
    return {str(row[0]) for row in rows if row[0] is not None}


def _iter_model_classes(module: Any) -> list[type[Any]]:
    classes: list[type[Any]] = []
    for _, obj in pyinspect.getmembers(module, pyinspect.isclass):
        if obj.__module__ != module.__name__:
            continue
        if hasattr(obj, "__tablename__") and hasattr(obj, "__table__"):
            classes.append(obj)
    return classes


def _iter_view_classes(module: Any) -> list[type[Any]]:
    classes: list[type[Any]] = []
    for _, obj in pyinspect.getmembers(module, pyinspect.isclass):
        if obj.__module__ != module.__name__:
            continue
        if hasattr(obj, "__viewname__"):
            classes.append(obj)
    return classes


def _extract_wrapped_routines(module: Any, helper_name: str) -> set[str]:
    source = pyinspect.getsource(module)
    tree = ast.parse(source)
    names: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Name):
            continue
        if node.func.id != helper_name:
            continue
        if len(node.args) < 2:
            continue
        second_arg = node.args[1]
        if isinstance(second_arg, ast.Constant) and isinstance(second_arg.value, str):
            names.add(second_arg.value)
    return names


def _implemented_model_tables(model_module_name: str) -> set[str]:
    module = importlib.import_module(model_module_name)
    return {str(cls.__tablename__) for cls in _iter_model_classes(module)}


def _implemented_view_names(view_module_name: str) -> set[str]:
    module = importlib.import_module(view_module_name)
    return {str(cls.__viewname__) for cls in _iter_view_classes(module)}


def _implemented_procedures(component_map: dict[str, str]) -> set[str]:
    scripts_module_name = component_map.get("scripts")
    if not scripts_module_name:
        return set()
    module = importlib.import_module(scripts_module_name)
    scripts = getattr(module, "STORED_PROCEDURES", None)
    if not isinstance(scripts, dict):
        raise AssertionError(f"{scripts_module_name} must define a STORED_PROCEDURES dictionary")
    return {str(name) for name in scripts}


def _implemented_funcs(component_map: dict[str, str]) -> set[str]:
    funcs_module_name = component_map.get("funcs")
    if not funcs_module_name:
        return set()
    module = importlib.import_module(funcs_module_name)
    funcs = getattr(module, "FUNCTIONS", None)
    if not isinstance(funcs, dict):
        raise AssertionError(f"{funcs_module_name} must define a FUNCTIONS dictionary")
    return {str(name) for name in funcs}


@pytest.mark.parametrize(("_db_module_name", "component_map"), MODULE_COMPONENTS.items())
def test_script_registry_matches_wrapped_scripts(
    _db_module_name: str, component_map: dict[str, str]
) -> None:
    scripts_module_name = component_map.get("scripts")
    if not scripts_module_name:
        return

    module = importlib.import_module(scripts_module_name)
    scripts = getattr(module, "STORED_PROCEDURES", None)
    assert isinstance(
        scripts, dict
    ), f"{scripts_module_name} must define a STORED_PROCEDURES dictionary"

    expected_scripts = _extract_wrapped_routines(module, "run_script")
    assert _normalize({str(name) for name in scripts}) == _normalize(expected_scripts)


def _db_object_names(session: Session, routine_types: tuple[str, ...]) -> set[str]:
    type_filters = ", ".join(f"'{routine_type}'" for routine_type in routine_types)
    query = (
        "SELECT name "
        "FROM sys.objects "
        "WHERE schema_id = SCHEMA_ID('dbo') "
        f"AND type IN ({type_filters}) "
        "AND is_ms_shipped = 0 "
        "AND create_date < '2016-01-01'"
    )
    return _query_names(session, query)


@pytest.mark.parametrize(("db_module_name", "component_map"), MODULE_COMPONENTS.items())
def test_all_implemented_model_columns_exist_in_live_tables(
    db_module_name: str, component_map: dict[str, str]
) -> None:
    model_module_name = component_map.get("models")
    if not model_module_name:
        return

    env_var = MODULE_ENV_VARS[db_module_name]
    model_module = importlib.import_module(model_module_name)
    model_classes = _iter_model_classes(model_module)

    with _session_for_module(db_module_name, env_var) as session:
        for model_class in model_classes:
            table_name = str(model_class.__tablename__)
            class_name = str(model_class.__name__)

            table_columns = _query_names(
                session,
                "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS "
                f"WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = '{table_name}'",
            )
            assert (
                table_columns
            ), f"Missing table dbo.{table_name} for model {model_module_name}.{class_name}"

            expected_columns = {str(column.name) for column in model_class.__table__.columns}
            expected_columns = expected_columns - KNOWN_SYNTHETIC_COLUMNS.get(
                (model_module_name, class_name),
                set(),
            )
            missing = _normalize(expected_columns) - _normalize(table_columns)
            assert not missing, (
                f"Missing columns in dbo.{table_name} for {model_module_name}.{class_name}: "
                f"{sorted(missing)}"
            )


@pytest.mark.parametrize(("db_module_name", "component_map"), MODULE_COMPONENTS.items())
def test_all_implemented_views_exist_in_live_database(
    db_module_name: str, component_map: dict[str, str]
) -> None:
    view_module_name = component_map.get("views")
    if not view_module_name:
        return

    env_var = MODULE_ENV_VARS[db_module_name]
    implemented_views = _implemented_view_names(view_module_name)

    with _session_for_module(db_module_name, env_var) as session:
        db_views = _query_names(
            session,
            "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'dbo'",
        )

    missing = _normalize(implemented_views) - _normalize(db_views)
    assert not missing, f"Implemented views missing in DB for {db_module_name}: {sorted(missing)}"


@pytest.mark.parametrize(("db_module_name", "component_map"), MODULE_COMPONENTS.items())
def test_all_functions_are_implemented_in_vida_py(
    db_module_name: str, component_map: dict[str, str]
) -> None:
    env_var = MODULE_ENV_VARS[db_module_name]
    implemented_functions = _implemented_funcs(component_map)
    normalized_impl_functions = _normalize(implemented_functions)

    with _session_for_module(db_module_name, env_var) as session:
        db_functions = _db_object_names(session, ("FN", "IF", "TF"))

    missing_functions = {
        e for e in db_functions if e.strip().lower() not in normalized_impl_functions
    }

    assert (
        not missing_functions
    ), f"Unimplemented functions for {db_module_name}: {sorted(missing_functions)}. "


@pytest.mark.parametrize(("db_module_name", "component_map"), MODULE_COMPONENTS.items())
def test_all_stored_procedures_are_implemented_in_vida_py(
    db_module_name: str, component_map: dict[str, str]
) -> None:
    env_var = MODULE_ENV_VARS[db_module_name]
    implemented_procedures = _implemented_procedures(component_map)
    normalized_impl_procedures = _normalize(implemented_procedures)

    with _session_for_module(db_module_name, env_var) as session:
        db_procedures = _db_object_names(session, ("P",))

    missing_procedures = {
        e for e in db_procedures if e.strip().lower() not in normalized_impl_procedures
    }

    assert (
        not missing_procedures
    ), f"Unimplemented procedures for {db_module_name}: {sorted(missing_procedures)}. Found: {implemented_procedures}"


def test_all_tables_are_implemented_in_vida_py() -> None:
    for db_module_name, component_map in MODULE_COMPONENTS.items():
        env_var = MODULE_ENV_VARS[db_module_name]

        implemented_tables = (
            _implemented_model_tables(component_map["models"])
            if "models" in component_map
            else set()
        )

        with _session_for_module(db_module_name, env_var) as session:
            db_tables = _query_names(
                session,
                "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' "
                "AND TABLE_TYPE = 'BASE TABLE'",
            )
        missing_tables = (
            _normalize(db_tables) - _normalize(implemented_tables) - _normalize(SYSTEM_TABLES)
        )

        assert (
            not missing_tables
        ), f"Unimplemented tables for {db_module_name}: {sorted(missing_tables)}"
