import pyodbc

from model_info import ENGINES_BY_NAME, MODELS_BY_NAME
from sql_funcs import get_profile

SERVER = "(local)"
DATABASE = "carcom"
USERNAME = "Asuser"
PASSWORD = "GunnarS3g3"

connectionString = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

profiles = get_profile(
    cursor,
    year=2650,  # 2004
    market=2743,  # AME
    steering=2750,  # LHD
    transmission=2640,  # AW50/51 AWD
    engine=2732,  # B5254T2
    model=2687,  # "V70 XC (01-) / XC70 (-07)"
)

print(profiles)
