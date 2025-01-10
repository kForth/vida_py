import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from vida_py.carcom.funcs import *
from vida_py.carcom.models import *
from vida_py.carcom.scripts import *

db: Engine = create_engine(os.getenv("VIDA_CARCOM_DB_URI"))
Session: sessionmaker = sessionmaker(bind=db)
