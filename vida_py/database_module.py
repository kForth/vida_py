"""Lazy database module initialization helpers for VIDA subpackages."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from typing import Any, cast

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.engine.url import make_url
from sqlalchemy.orm import Session, sessionmaker

from vida_py.util import get_required_db_uri


class DatabaseModule:
    def __init__(self, variable_name: str):
        self.variable_name = variable_name
        self._engine: Engine | None = None
        self._session_factory: sessionmaker | None = None

    def create_engine_from_env(
        self, *, variable_name: str | None = None, **engine_kwargs: Any
    ) -> Engine:
        return create_engine(
            get_required_db_uri(variable_name or self.variable_name), **engine_kwargs
        )

    def create_engine_from_url(self, url: str, **engine_kwargs: Any) -> Engine:
        return create_engine(make_url(url), **engine_kwargs)

    def create_session_factory(
        self,
        *,
        engine: Engine | None = None,
        url: str | None = None,
        **engine_kwargs: Any,
    ) -> sessionmaker:
        if engine is None:
            engine = (
                self.create_engine_from_url(url, **engine_kwargs)
                if url is not None
                else self.create_engine_from_env(**engine_kwargs)
            )
        return sessionmaker(bind=engine)

    def initialize(
        self,
        *,
        engine: Engine | None = None,
        url: str | None = None,
        **engine_kwargs: Any,
    ) -> sessionmaker:
        if engine is None:
            engine = (
                self.create_engine_from_url(url, **engine_kwargs)
                if url is not None
                else self.create_engine_from_env(**engine_kwargs)
            )

        self._engine = engine
        self._session_factory = sessionmaker(bind=engine)
        return self._session_factory

    def get_engine(self) -> Engine:
        if self._engine is None:
            self.initialize()
        assert self._engine is not None
        return self._engine

    def get_session_factory(self) -> sessionmaker:
        if self._session_factory is None:
            self.initialize()
        assert self._session_factory is not None
        return self._session_factory

    def dispose_engine(self) -> None:
        if self._engine is not None:
            self._engine.dispose()

    def reset(self, *, dispose_engine: bool = True) -> None:
        if dispose_engine:
            self.dispose_engine()
        self._engine = None
        self._session_factory = None

    def create_session(self, **session_kwargs: Any) -> Session:
        return cast("Session", self.get_session_factory()(**session_kwargs))
