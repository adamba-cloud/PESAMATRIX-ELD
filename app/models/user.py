import sqlite3, hashlib
from datetime import datetime

def hash_password(p): 
    return hashlib.sha256(p.encode()).hexdigest()

def create_user_table(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT,
        email TEXT,
        password TEXT,
        role TEXT,
        status TEXT,
        account_number TEXT
    )
    """)

    conn.commit()
    conn.close()
