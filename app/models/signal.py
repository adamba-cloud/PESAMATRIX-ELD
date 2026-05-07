
import sqlite3

def create_signal_table(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS signals(
        id INTEGER PRIMARY KEY,
        asset TEXT,
        entry TEXT,
        tp TEXT,
        sl TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()
