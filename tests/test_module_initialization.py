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

