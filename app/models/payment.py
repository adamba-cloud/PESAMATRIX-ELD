import sqlite3
from datetime import datetime

def create_payment_table(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments(
        id INTEGER PRIMARY KEY,
        phone TEXT,
        mpesa TEXT,
        amount TEXT,
        plan TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()
