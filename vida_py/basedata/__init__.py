import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from vida_py.basedata.funcs import *
from vida_py.basedata.models import *
from vida_py.basedata.scripts import *

db: Engine = create_engine(os.getenv("VIDA_BASEDATA_DB_URI"))
Session: sessionmaker = sessionmaker(bind=db)
