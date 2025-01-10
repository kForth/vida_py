import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from vida_py.images.models import *
from vida_py.images.scripts import *

db: Engine = create_engine(os.getenv("VIDA_IMAGES_DB_URI"))
Session: sessionmaker = sessionmaker(bind=db)
