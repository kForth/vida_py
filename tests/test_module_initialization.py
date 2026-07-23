"""Tests for lazy submodule initialization and package exports."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

import importlib
import sys

import pytest

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

SESSION_EXPORTS = {
    "AccessServerSession": "vida_py.access",
    "BaseDataSession": "vida_py.basedata",
    "CarComSession": "vida_py.carcom",
    "DiagRepoSession": "vida_py.diag",
    "DiagSessionSession": "vida_py.session",
    "DiceTimingSession": "vida_py.timing",
    "EpcSession": "vida_py.epc",
    "ImageRepoSession": "vida_py.images",
    "ServiceRepoSession": "vida_py.service",
}


@pytest.mark.parametrize(("module_name", "env_var"), MODULE_ENV_VARS.items())
def test_database_submodules_import_without_touching_env(
    monkeypatch: pytest.MonkeyPatch, module_name: str, env_var: str
) -> None:
    monkeypatch.delenv(env_var, raising=False)
    sys.modules.pop(module_name, None)

    module = importlib.import_module(module_name)

    assert callable(module.Session)
    assert callable(module.create_session)
    assert callable(module.create_engine_from_env)
    assert callable(module.create_engine_from_url)
    assert callable(module.create_session_factory)
    assert callable(module.initialize)
    assert callable(module.get_engine)
    assert callable(module.get_session_factory)


def test_top_level_package_exports_sessions_lazily() -> None:
    sys.modules.pop("vida_py", None)
    sys.modules.pop("vida_py.access", None)

    package = importlib.import_module("vida_py")

    assert "vida_py.access" not in sys.modules

    session_factory = package.AccessServerSession

    assert callable(session_factory)
    assert "vida_py.access" in sys.modules


def test_top_level_package_rejects_unknown_export() -> None:
    sys.modules.pop("vida_py", None)
    package = importlib.import_module("vida_py")

    with pytest.raises(AttributeError, match="Nope"):
        _ = package.Nope


def test_top_level_package_exports_all_session_aliases() -> None:
    sys.modules.pop("vida_py", None)
    package = importlib.import_module("vida_py")

    assert set(package.__all__) == {
        "AccessServerSession",
        "BaseDataSession",
        "CarComSession",
        "DiagRepoSession",
        "DiagSessionSession",
        "DiceTimingSession",
        "EpcSession",
        "ImageRepoSession",
        "ServiceRepoSession",
    }


@pytest.mark.parametrize(("export_name", "module_name"), SESSION_EXPORTS.items())
def test_top_level_session_aliases_resolve_to_submodule_session(
    export_name: str, module_name: str
) -> None:
    sys.modules.pop("vida_py", None)
    sys.modules.pop(module_name, None)

    package = importlib.import_module("vida_py")
    exported_session = getattr(package, export_name)
    submodule = importlib.import_module(module_name)

    assert exported_session is submodule.Session


@pytest.mark.parametrize(("export_name", "module_name"), SESSION_EXPORTS.items())
def test_top_level_session_aliases_are_stable(export_name: str, module_name: str) -> None:
    sys.modules.pop("vida_py", None)
    sys.modules.pop(module_name, None)

    package = importlib.import_module("vida_py")

    first = getattr(package, export_name)
    second = getattr(package, export_name)

    assert first is second
