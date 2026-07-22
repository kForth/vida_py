"""Tests for database module helpers and configuration validation."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from typing import Any, cast

import pytest

from vida_py.database_module import DatabaseModule
from vida_py.util import get_required_db_uri


def test_get_required_db_uri_raises_for_missing_variable(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("VIDA_TEST_DB_URI", raising=False)

    with pytest.raises(RuntimeError, match="VIDA_TEST_DB_URI"):
        get_required_db_uri("VIDA_TEST_DB_URI")


def test_get_required_db_uri_raises_for_invalid_uri(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("VIDA_TEST_DB_URI", "not a sqlalchemy url")

    with pytest.raises(ValueError, match="VIDA_TEST_DB_URI"):
        get_required_db_uri("VIDA_TEST_DB_URI")


def test_database_module_create_engine_from_env_uses_validated_uri(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")
    captured: dict[str, Any] = {}

    def fake_create_engine(url: str, **engine_kwargs: Any) -> object:
        captured["url"] = url
        captured["engine_kwargs"] = engine_kwargs
        return object()

    monkeypatch.setattr("vida_py.database_module.create_engine", fake_create_engine)
    monkeypatch.setenv("VIDA_TEST_DB_URI", "sqlite+pysqlite:///:memory:")

    module.create_engine_from_env(pool_pre_ping=True)

    assert captured == {
        "url": "sqlite+pysqlite:///:memory:",
        "engine_kwargs": {"pool_pre_ping": True},
    }


def test_database_module_create_session_uses_cached_session_factory(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")
    expected_session = object()
    call_count = 0

    class FakeSessionFactory:
        def __call__(self, **session_kwargs: Any) -> object:
            assert session_kwargs == {"expire_on_commit": False}
            return expected_session

    def fake_initialize(**_: Any) -> FakeSessionFactory:
        nonlocal call_count
        call_count += 1
        fake_factory = FakeSessionFactory()
        module._session_factory = cast("Any", fake_factory)
        return fake_factory

    monkeypatch.setattr(module, "initialize", fake_initialize)

    first_session = module.create_session(expire_on_commit=False)
    second_session = module.create_session(expire_on_commit=False)

    assert first_session is expected_session
    assert second_session is expected_session
    assert call_count == 1
