import pyodbc
import time

def InsertBBDD(InsertQuery):
    cnxn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=MKTCRM;"
    "Database=RPyA;"
    "Trusted_Connection=yes")

    fecha = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Insertando en la bbdd a las {fecha}")
    cursor = cnxn.cursor()
    cursor.execute(InsertQuery)
    cnxn.commit()

def truncateBBDD():
    cnxn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=MKTCRM;"
    "Database=RPyA;"
    "Trusted_Connection=yes")
    truncateQuery = "truncate table [RPyA].[dbo].[RPyA_2MARES]"
    fecha = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Truncating tabla a las {fecha}")
    cursor = cnxn.cursor()
    cursor.execute(truncateQuery)
    cnxn.commit()