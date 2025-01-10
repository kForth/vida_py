import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from vida_py.access.models import *
from vida_py.access.scripts import *

db: Engine = create_engine(os.getenv("VIDA_ACCESS_DB_URI"))
Session: sessionmaker = sessionmaker(bind=db)
