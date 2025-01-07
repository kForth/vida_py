import csv
import os

import pyodbc

SERVER = "(local)"
USERNAME = "Asuser"
PASSWORD = "GunnarS3g3"

DATABASE = "carcom"

connectionString = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

cursor.execute("SELECT DISTINCT [TABLE_NAME] FROM INFORMATION_SCHEMA.TABLES")
for _table in cursor.fetchall():

    table = _table.TABLE_NAME
    cursor.execute(f"SELECT * FROM [{table}]")
    rows = cursor.fetchall()

    outpath = f"tables/{DATABASE}/{table}.csv"
    os.makedirs(os.path.split(outpath)[0], exist_ok=True)
    with open(outpath, "w+", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([x[0] for x in cursor.description])
        for row in rows:
            writer.writerow(row)

cursor.close()
conn.close()
