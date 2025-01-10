import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from vida_py.diag.funcs import *
from vida_py.diag.models import *
from vida_py.diag.scripts import *

db: Engine = create_engine(os.getenv("VIDA_DIAG_DB_URI"))
Session: sessionmaker = sessionmaker(bind=db)
