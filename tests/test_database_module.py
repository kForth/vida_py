"""Tests for database module helpers and configuration validation."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from typing import Any

import pytest
from sqlalchemy.engine import Engine

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


def test_database_module_create_engine_from_env_can_override_variable_name(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = DatabaseModule("VIDA_DEFAULT_DB_URI")
    captured: dict[str, Any] = {}

    def fake_create_engine(url: str, **engine_kwargs: Any) -> object:
        captured["url"] = url
        captured["engine_kwargs"] = engine_kwargs
        return object()

    monkeypatch.setattr("vida_py.database_module.create_engine", fake_create_engine)
    monkeypatch.setenv("VIDA_OVERRIDE_DB_URI", "sqlite+pysqlite:///:memory:")

    module.create_engine_from_env(variable_name="VIDA_OVERRIDE_DB_URI", pool_pre_ping=True)

    assert captured == {
        "url": "sqlite+pysqlite:///:memory:",
        "engine_kwargs": {"pool_pre_ping": True},
    }


def test_database_module_create_engine_from_url_validates_and_builds_engine() -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")

    engine = module.create_engine_from_url("sqlite+pysqlite:///:memory:")

    assert isinstance(engine, Engine)
    assert engine.url.database == ":memory:"


def test_database_module_initialize_and_getters_cache_the_engine() -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")
    engine = module.create_engine_from_url("sqlite+pysqlite:///:memory:")

    session_factory = module.initialize(engine=engine)

    assert module.get_engine() is engine
    assert module.get_session_factory() is session_factory


def test_database_module_create_session_factory_uses_engine_argument() -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")
    engine = module.create_engine_from_url("sqlite+pysqlite:///:memory:")

    session_factory = module.create_session_factory(engine=engine)

    session = session_factory()
    assert session.bind is engine
    session.close()


def test_database_module_initialize_uses_url_argument() -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")

    session_factory = module.initialize(url="sqlite+pysqlite:///:memory:")

    assert module.get_engine().url.database == ":memory:"
    assert session_factory is module.get_session_factory()


def test_database_module_create_session_returns_session_object() -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")
    engine = module.create_engine_from_url("sqlite+pysqlite:///:memory:")
    module.initialize(engine=engine)

    session = module.create_session()

    assert session.bind is engine
    session.close()


def test_database_module_create_session_uses_session_factory(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")
    expected_session = object()

    class FakeSessionFactory:
        def __call__(self, **session_kwargs: Any) -> object:
            assert session_kwargs == {"expire_on_commit": False}
            return expected_session

    fake_factory = FakeSessionFactory()
    monkeypatch.setattr(DatabaseModule, "get_session_factory", lambda self: fake_factory)

    first_session = module.create_session(expire_on_commit=False)
    second_session = module.create_session(expire_on_commit=False)

    assert first_session is expected_session
    assert second_session is expected_session


def test_database_module_get_engine_initializes_lazily(monkeypatch: pytest.MonkeyPatch) -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")
    engine = module.create_engine_from_url("sqlite+pysqlite:///:memory:")
    session_factory = module.create_session_factory(engine=engine)

    def fake_initialize() -> Any:
        object.__setattr__(module, "_engine", engine)
        object.__setattr__(module, "_session_factory", session_factory)
        return session_factory

    monkeypatch.setattr(module, "initialize", fake_initialize)

    assert module.get_engine() is engine


def test_database_module_get_session_factory_initializes_lazily(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")
    engine = module.create_engine_from_url("sqlite+pysqlite:///:memory:")
    expected_factory = module.create_session_factory(engine=engine)

    def fake_initialize() -> Any:
        object.__setattr__(module, "_engine", engine)
        object.__setattr__(module, "_session_factory", expected_factory)
        return expected_factory

    monkeypatch.setattr(module, "initialize", fake_initialize)

    assert module.get_session_factory() is expected_factory


def test_database_module_create_session_factory_uses_url_when_no_engine(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")
    engine = module.create_engine_from_url("sqlite+pysqlite:///:memory:")

    def fake_create_engine_from_url(url: str, **engine_kwargs: Any) -> Engine:
        assert url == "sqlite+pysqlite:///:memory:"
        assert engine_kwargs == {"pool_pre_ping": True}
        return engine

    monkeypatch.setattr(module, "create_engine_from_url", fake_create_engine_from_url)

    session_factory = module.create_session_factory(
        url="sqlite+pysqlite:///:memory:",
        pool_pre_ping=True,
    )

    session = session_factory()
    assert session.bind is engine
    session.close()


def test_database_module_create_session_factory_uses_env_when_no_engine_or_url(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")
    engine = module.create_engine_from_url("sqlite+pysqlite:///:memory:")

    def fake_create_engine_from_env(**engine_kwargs: Any) -> Engine:
        assert engine_kwargs == {"pool_pre_ping": True}
        return engine

    monkeypatch.setattr(module, "create_engine_from_env", fake_create_engine_from_env)

    session_factory = module.create_session_factory(pool_pre_ping=True)

    session = session_factory()
    assert session.bind is engine
    session.close()


def test_database_module_initialize_uses_env_when_no_engine_or_url(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")
    engine = module.create_engine_from_url("sqlite+pysqlite:///:memory:")

    def fake_create_engine_from_env(**engine_kwargs: Any) -> Engine:
        assert engine_kwargs == {"pool_pre_ping": True}
        return engine

    monkeypatch.setattr(module, "create_engine_from_env", fake_create_engine_from_env)

    session_factory = module.initialize(pool_pre_ping=True)

    assert module.get_engine() is engine
    assert module.get_session_factory() is session_factory


def test_database_module_dispose_engine_calls_engine_dispose_once() -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")

    class FakeEngine:
        def __init__(self) -> None:
            self.calls = 0

        def dispose(self) -> None:
            self.calls += 1

    fake_engine = FakeEngine()
    object.__setattr__(module, "_engine", fake_engine)

    module.dispose_engine()

    assert fake_engine.calls == 1


def test_database_module_dispose_engine_is_noop_when_uninitialized() -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")

    module.dispose_engine()

    assert module._engine is None


def test_database_module_reset_disposes_and_clears_cached_state() -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")

    class FakeEngine:
        def __init__(self) -> None:
            self.calls = 0

        def dispose(self) -> None:
            self.calls += 1

    fake_engine = FakeEngine()
    fake_session_factory = object()

    object.__setattr__(module, "_engine", fake_engine)
    object.__setattr__(module, "_session_factory", fake_session_factory)

    module.reset()

    assert fake_engine.calls == 1
    assert module._engine is None
    assert module._session_factory is None


def test_database_module_reset_can_skip_dispose() -> None:
    module = DatabaseModule("VIDA_TEST_DB_URI")

    class FakeEngine:
        def __init__(self) -> None:
            self.calls = 0

        def dispose(self) -> None:
            self.calls += 1

    fake_engine = FakeEngine()

    object.__setattr__(module, "_engine", fake_engine)
    object.__setattr__(module, "_session_factory", object())

    module.reset(dispose_engine=False)

    assert fake_engine.calls == 0
    assert module._engine is None
    assert module._session_factory is None
