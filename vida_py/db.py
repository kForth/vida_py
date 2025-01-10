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

ServerAccess = sessionmaker(bind=access_db)  # AccessServer
BaseData = sessionmaker(bind=basedata_db)  # basedata
CarCom = sessionmaker(bind=carcom_db)  # carcom
DiagRepo = sessionmaker(bind=diag_db)  # DiagSwdlRepository
DiagSession = sessionmaker(bind=session_db)  # DiagSwdlSession
Timing = sessionmaker(bind=timing_db)  # DiceTiming
Epc = sessionmaker(bind=epc_db)  # EPC
ImageRepo = sessionmaker(bind=images_db)  # ImageRepository
ServiceRepo = sessionmaker(bind=service_db)  # servicerep_en
