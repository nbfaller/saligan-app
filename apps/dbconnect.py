import psycopg2
import pandas as pd
import os

class dbcreds:
    local = dict(
        host = 'localhost',
        database = 'saligan-db',
        user = 'postgres',
        port = 5432,
        password = 'password'
    )

def getdblocation():
    local = True
    if local:
        # Define connection details
        creds = dbcreds.local
        db = psycopg2.connect(
            host = creds['host'],
            database = creds['database'],
            user = creds['user'],
            port = creds['port'],
            password = creds['password']
        )
    else:
        DATABASE_URL = os.environ.get('DATABASE_URL')
        db = psycopg2.connect(DATABASE_URL, sslmode = 'require')
    # Return connection details
    return db

def modifydb(query, params = None):
    db = getdblocation()
    cursor = db.cursor()
    cursor.execute(query, params)
    db.commit()
    cursor.close()
    db.close()

def querydb(query, params = None, cols = None):
    db = getdblocation()
    cursor = db.cursor()
    cursor.execute(query, params)
    rows = pd.DataFrame(cursor.fetchall(), columns = cols)
    cursor.close()
    db.close()
    return rows