import sqlalchemy

SERVER = "(local)"
USERNAME = "Asuser"
PASSWORD = "GunnarS3g3"

def create_engine(db: str) -> sqlalchemy.Engine:
    return sqlalchemy.create_engine(f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{db}?driver=ODBC+Driver+17+for+SQL+Server").connect()

access = create_engine("AccessServer")
basedata = create_engine("basedata")
carcom = create_engine("carcom")
diag = create_engine("DiagSwdlRepository")
session = create_engine("DiagSwdlSession")
timing = create_engine("DiceTiming")
images = create_engine("ImageRepository")
service = create_engine("servicerepository")
