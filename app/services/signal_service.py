import sqlite3

def create_signal(db, asset, entry, tp, sl):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO signals(asset, entry, tp, sl, status)
        VALUES(?,?,?,?,?)
    """, (asset, entry, tp, sl, "ACTIVE"))

    conn.commit()
    conn.close()


def get_signals(db):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    data = cur.execute("SELECT * FROM signals ORDER BY id DESC").fetchall()

    conn.close()
    return data
