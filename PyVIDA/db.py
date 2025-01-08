import os

from sqlalchemy import Engine, create_engine


def _engine(uri: str) -> Engine:
    return create_engine(uri).connect()


access = _engine(os.getenv("VIDA_ACCESSS_DB_URI"))
basedata = _engine(os.getenv("VIDA_BASEDATA_DB_URI"))
carcom = _engine(os.getenv("VIDA_CARCOM_DB_URI"))
diag = _engine(os.getenv("VIDA_DIAG_DB_URI"))
session = _engine(os.getenv("VIDA_SESSION_DB_URI"))
timing = _engine(os.getenv("VIDA_TIMING_DB_URI"))
# epc = _engine(os.getenv("VIDA_EPC_DB_URI"))
images = _engine(os.getenv("VIDA_IMAGES_DB_URI"))
service = _engine(os.getenv("VIDA_SERVICE_DB_URI"))
