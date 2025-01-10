import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

access_db = create_engine(os.getenv("VIDA_ACCESS_DB_URI"))
basedata_db = create_engine(os.getenv("VIDA_BASEDATA_DB_URI"))
carcom_db = create_engine(os.getenv("VIDA_CARCOM_DB_URI"))
diag_db = create_engine(os.getenv("VIDA_DIAG_DB_URI"))
session_db = create_engine(os.getenv("VIDA_SESSION_DB_URI"))
timing_db = create_engine(os.getenv("VIDA_TIMING_DB_URI"))
epc_db = create_engine(os.getenv("VIDA_EPC_DB_URI"))
images_db = create_engine(os.getenv("VIDA_IMAGES_DB_URI"))
service_db = create_engine(os.getenv("VIDA_SERVICE_DB_URI"))

access_session = sessionmaker(bind=access_db)
basedata_session = sessionmaker(bind=basedata_db)
carcom_session = sessionmaker(bind=carcom_db)
diag_session = sessionmaker(bind=diag_db)
session_session = sessionmaker(bind=session_db)
timing_session = sessionmaker(bind=timing_db)
epc_session = sessionmaker(bind=epc_db)
images_session = sessionmaker(bind=images_db)
service_session = sessionmaker(bind=service_db)
