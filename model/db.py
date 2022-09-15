import sqlite3

FILE_DB = 'database/system_database.db'

def connect():
    conn = sqlite3.connect(FILE_DB)
    return conn