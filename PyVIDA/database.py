from sqlalchemy import Engine, create_engine

SERVER = "(local)"
USERNAME = "Asuser"
PASSWORD = "GunnarS3g3"


def create_engine(db: str) -> Engine:
    return create_engine(
        f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{db}?driver=ODBC+Driver+17+for+SQL+Server"
    ).connect()


access = create_engine("AccessServer")
basedata = create_engine("basedata")
carcom = create_engine("carcom")
diag = create_engine("DiagSwdlRepository")
session = create_engine("DiagSwdlSession")
timing = create_engine("DiceTiming")
epc = create_engine("EPC")
images = create_engine("ImageRepository")
service = create_engine("servicerep_en-US")  # "servicerepository"
