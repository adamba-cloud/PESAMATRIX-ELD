import sqlite3

def create_content_table(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS content(
        id INTEGER PRIMARY KEY,
        type TEXT,
        link TEXT,
        title TEXT
    )
    """)

    conn.commit()
    conn.close()
