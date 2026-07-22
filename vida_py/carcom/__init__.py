"""Session factory and public exports for the `carcom` VIDA database module."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from typing import Any

from sqlalchemy.orm import Session as OrmSession

from vida_py.database_module import DatabaseModule

_DATABASE = DatabaseModule("VIDA_CARCOM_DB_URI")

create_engine_from_env = _DATABASE.create_engine_from_env
create_engine_from_url = _DATABASE.create_engine_from_url
create_session_factory = _DATABASE.create_session_factory
initialize = _DATABASE.initialize
get_engine = _DATABASE.get_engine
get_session_factory = _DATABASE.get_session_factory


def create_session(**session_kwargs: Any) -> OrmSession:
    return _DATABASE.create_session(**session_kwargs)


Session = create_session


__all__ = [
    "Session",
    "create_engine_from_env",
    "create_engine_from_url",
    "create_session",
    "create_session_factory",
    "get_engine",
    "get_session_factory",
    "initialize",
]
