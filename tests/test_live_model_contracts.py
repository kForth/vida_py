"""Live integration tests validating ORM model contracts against VIDA databases."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

import importlib
import inspect as pyinspect
import os
import sys
from collections.abc import Generator
from contextlib import contextmanager
from typing import Any, cast

import pytest
from sqlalchemy import inspect
from sqlalchemy.engine import Engine
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

MODEL_MODULES = {
    "vida_py.access": "vida_py.access.models",
    "vida_py.basedata": "vida_py.basedata.models",
    "vida_py.carcom": "vida_py.carcom.models",
    "vida_py.diag": "vida_py.diag.models",
    "vida_py.epc": "vida_py.epc.models",
    "vida_py.images": "vida_py.images.models",
    "vida_py.service": "vida_py.service.models",
    "vida_py.session": "vida_py.session.models",
    "vida_py.timing": "vida_py.timing.models",
}

VIEW_MODULES = {
    "vida_py.basedata": "vida_py.basedata.views",
    "vida_py.diag": "vida_py.diag.views",
    "vida_py.timing": "vida_py.timing.views",
}

# Some classes use synthetic key columns to satisfy ORM mapping where the DB object has no PK.
# Those columns are intentionally not present in the underlying DB object.
KNOWN_SYNTHETIC_COLUMNS: dict[tuple[str, str], set[str]] = {
    ("vida_py.diag.models", "EcuDescription"): {"id"},
    ("vida_py.diag.models", "IEGenericComponent"): {"id"},
    ("vida_py.diag.models", "SmartToolScript"): {"id"},
    ("vida_py.session.models", "ActionItem"): {"id"},
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


def _engine_for_db_module(db_module_name: str) -> Engine:
    env_var = MODULE_ENV_VARS[db_module_name]
    with _session_for_module(db_module_name, env_var) as session:
        return cast("Engine", session.get_bind())


def _table_columns(engine: Engine, table_name: str) -> set[str]:
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name, schema="dbo")
    return {str(col["name"]) for col in columns}


def _normalize_columns(columns: set[str]) -> set[str]:
    return {column.lower() for column in columns}


def _iter_declared_model_classes(module: Any) -> list[type[Any]]:
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


@pytest.mark.parametrize(("db_module_name", "model_module_name"), MODEL_MODULES.items())
def test_live_all_model_columns_exist_in_tables(
    db_module_name: str, model_module_name: str
) -> None:
    model_module = importlib.import_module(model_module_name)
    model_classes = _iter_declared_model_classes(model_module)
    assert model_classes

    engine = _engine_for_db_module(db_module_name)
    inspector = inspect(engine)

    for model_class in model_classes:
        table_name = str(model_class.__tablename__)
        class_name = str(model_class.__name__)
        assert inspector.has_table(
            table_name, schema="dbo"
        ), f"Missing table dbo.{table_name} for model {model_module_name}.{class_name}"

        expected_columns = {str(column.name) for column in model_class.__table__.columns}
        expected_columns = expected_columns - KNOWN_SYNTHETIC_COLUMNS.get(
            (model_module_name, class_name),
            set(),
        )

        existing_columns = _table_columns(engine, table_name)
        missing_columns = _normalize_columns(expected_columns) - _normalize_columns(
            existing_columns
        )
        assert not missing_columns, (
            f"Missing columns in dbo.{table_name} for {model_module_name}.{class_name}: "
            f"{sorted(missing_columns)}"
        )


@pytest.mark.parametrize(("db_module_name", "view_module_name"), VIEW_MODULES.items())
def test_live_all_view_model_columns_exist_in_views(
    db_module_name: str, view_module_name: str
) -> None:
    view_module = importlib.import_module(view_module_name)
    view_classes = _iter_view_classes(view_module)
    assert view_classes

    engine = _engine_for_db_module(db_module_name)
    inspector = inspect(engine)

    for view_class in view_classes:
        view_name = str(view_class.__viewname__)
        class_name = str(view_class.__name__)
        assert inspector.has_table(
            view_name, schema="dbo"
        ), f"Missing view dbo.{view_name} for model {view_module_name}.{class_name}"

        expected_columns = {str(name) for name in getattr(view_class, "__annotations__", {})}
        existing_columns = _table_columns(engine, view_name)
        missing_columns = _normalize_columns(expected_columns) - _normalize_columns(
            existing_columns
        )
        assert not missing_columns, (
            f"Missing columns in dbo.{view_name} for {view_module_name}.{class_name}: "
            f"{sorted(missing_columns)}"
        )
