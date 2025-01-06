import json

import pyodbc

from sql_funcs import (
    get_block,
    get_block_children,
    get_profile_ecus,
    get_profiles_fuzzy,
)

# from model_info import ENGINES_BY_NAME, MODELS_BY_NAME

# year = 2004
# model = "V70 XC (01-) / XC70 (-07)"
# # model = "V70 (00-08)"
# engine = "B5254T2"

# _model = MODELS_BY_NAME[model]
# _engine = ENGINES_BY_NAME[engine]
# profile_str = f"mdl{_model}yr{year}eng{_engine}"
profile_id = 799
language = 19

BLOCK_DATA_TYPES = {
    1: "Signed",
    2: "Unsigned",
    3: "4-byte float",
    50: "Hex",
    51: "Ascii",
    52: "BCD",
    53: "BCD+Ascii",
}

SERVER = "(local)"
DATABASE = "carcom"
USERNAME = "Asuser"
PASSWORD = "GunnarS3g3"

connectionString = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

profiles = get_profiles_fuzzy(
    cursor,
    year=2650,
    market=2743,
    steering=2750,
    transmission=2640,
    engine=2732,
    model=2687,
)

ecus = sum((get_profile_ecus(cursor, e["id"]) for e in profiles), start=[])
# blocks = {ecu: get_blocks(cursor, ecu, language) for ecu in ecus}

children = sum((get_block_children(cursor, ecu) for ecu in ecus), start=[])
child_ids = {e["child_id"] for e in children}

all_blocks = [get_block(cursor, id, language) for id in child_ids]

cursor.close()
conn.close()

with open("blocks.json", "w+") as out:
    json.dump(all_blocks, out, indent=2)
