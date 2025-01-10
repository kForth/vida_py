import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from vida_py.epc.models import *

db: Engine = create_engine(os.getenv("VIDA_EPC_DB_URI"))
Session: sessionmaker = sessionmaker(bind=db)
