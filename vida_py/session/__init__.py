import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from vida_py.session.funcs import *
from vida_py.session.models import *
from vida_py.session.scripts import *

db: Engine = create_engine(os.getenv("VIDA_SESSION_DB_URI"))
Session: sessionmaker = sessionmaker(bind=db)
