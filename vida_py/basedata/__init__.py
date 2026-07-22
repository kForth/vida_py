"""Session factory and public exports for the basedata VIDA database module."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

db: Engine = create_engine(os.getenv("VIDA_BASEDATA_DB_URI") or "")

Session: sessionmaker = sessionmaker(bind=db)
