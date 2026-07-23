"""Tests for shared SQL helpers and thin wrapper functions."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from datetime import datetime
from typing import Any, cast

import pytest

from vida_py import util
from vida_py.session import funcs as session_funcs


class FakeResult:
    def __init__(self, *, rows: list[Any] | None = None, scalar: Any = None) -> None:
        self._rows = [] if rows is None else rows
        self._scalar = scalar

    def all(self) -> list[Any]:
        return self._rows

    def scalar_one_or_none(self) -> Any:
        return self._scalar


class FakeSession:
    def __init__(self, result: Any) -> None:
        self.result = result
        self.calls: list[tuple[Any, dict[str, Any]]] = []

    def execute(self, statement: Any, params: dict[str, Any]) -> Any:
        self.calls.append((statement, params))
        return self.result


def test_get_required_db_uri_returns_valid_value(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("VIDA_TEST_DB_URI", "sqlite+pysqlite:///:memory:")

    assert util.get_required_db_uri("VIDA_TEST_DB_URI") == "sqlite+pysqlite:///:memory:"


def test_run_script_builds_sql_and_parameters() -> None:
    result = object()
    session = cast("Any", FakeSession(result))

    returned = util.run_script(session, "CleanUp", DestDatabase="vida", Enabled=True)

    assert returned is result
    assert len(session.calls) == 1

    statement, params = session.calls[0]
    assert str(statement) == (
        "DECLARE @RC int\n"
        "EXECUTE @RC = [dbo].[CleanUp]\n"
        "@DestDatabase = :DestDatabase\n"
        ",@Enabled = :Enabled\n"
        "SELECT @RC"
    )
    assert params == {"DestDatabase": "vida", "Enabled": True}


def test_run_func_builds_sql_and_parameters() -> None:
    result = object()
    session = cast("Any", FakeSession(result))

    returned = util.run_func(session, "Split", "alpha", "beta")

    assert returned is result
    assert len(session.calls) == 1

    statement, params = session.calls[0]
    assert str(statement) == ("SELECT * FROM [dbo].[Split] (\n" ":0\n" ",:1\n" ")")
    assert params == {"0": "alpha", "1": "beta"}


def test_require_scalar_returns_value_and_raises_for_none() -> None:
    assert util.require_scalar(7, "GetValue") == 7

    with pytest.raises(ValueError, match="GetValue returned no rows"):
        util.require_scalar(None, "GetValue")


def test_run_func_scalar_returns_scalar_value(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_result = FakeResult(scalar=datetime(2026, 7, 23))

    def fake_run_func(session: Any, script: str, *args: Any) -> FakeResult:
        assert session == object_session
        assert script == "GetOrderDate"
        assert args == (123,)
        return fake_result

    object_session = cast("Any", object())
    monkeypatch.setattr(util, "run_func", fake_run_func)

    assert util.run_func_scalar(object_session, "GetOrderDate", 123) == datetime(2026, 7, 23)


def test_session_scalar_wrappers_delegate_to_shared_helper(monkeypatch: pytest.MonkeyPatch) -> None:
    object_session = cast("Any", object())
    captured: list[tuple[str, tuple[Any, ...]]] = []

    def fake_run_func_scalar(session: Any, script: str, *args: Any) -> Any:
        captured.append((script, args))
        assert session is object_session
        return {
            "GetOrderDate": datetime(2026, 7, 23),
            "GetStatus": "OK",
            "GetTransactionNbr": 42,
        }[script]

    monkeypatch.setattr(session_funcs, "run_func_scalar", fake_run_func_scalar)

    assert session_funcs.get_order_date(object_session, 321) == datetime(2026, 7, 23)
    assert session_funcs.get_status(object_session, 321) == "OK"
    assert session_funcs.get_transaction_nbr(object_session, 321) == 42

    assert captured == [
        ("GetOrderDate", (321,)),
        ("GetStatus", (321,)),
        ("GetTransactionNbr", (321,)),
    ]


def test_session_split_wrapper_converts_rows_to_strings(monkeypatch: pytest.MonkeyPatch) -> None:
    object_session = cast("Any", object())

    class FakeRows:
        def all(self) -> list[Any]:
            return [(1,), (datetime(2026, 7, 23),), (None,)]

    def fake_run_func(session: Any, script: str, *args: Any) -> FakeRows:
        assert session is object_session
        assert script == "Split"
        assert args == ("alpha", ",")
        return FakeRows()

    monkeypatch.setattr(session_funcs, "run_func", fake_run_func)

    assert session_funcs.split(object_session, "alpha", ",") == [
        "(1,)",
        "(datetime.datetime(2026, 7, 23, 0, 0),)",
        "(None,)",
    ]
