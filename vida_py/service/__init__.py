import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from vida_py.service.funcs import *
from vida_py.service.models import *
from vida_py.service.scripts import *

db: Engine = create_engine(os.getenv("VIDA_SERVICE_DB_URI"))
Session: sessionmaker = sessionmaker(bind=db)
