import sqlite3
import time


# =========================
# CREATE SIGNAL TABLE
# =========================
def create_signal_table(db_path):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS signals (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        asset TEXT NOT NULL,
        entry TEXT NOT NULL,
        tp TEXT NOT NULL,
        sl TEXT NOT NULL,

        # lifecycle status
        status TEXT DEFAULT 'Upcoming',

        # timestamps (SaaS tracking)
        created_at INTEGER DEFAULT (strftime('%s','now')),
        updated_at INTEGER DEFAULT (strftime('%s','now'))

    )
    """)

    conn.commit()
    conn.close()


# =========================
# UPDATE SIGNAL STATUS
# =========================
def update_signal_status(db_path, signal_id, status):

    allowed_status = ["Upcoming", "Running", "Expired"]

    if status not in allowed_status:
        return False

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        UPDATE signals
        SET status = ?,
            updated_at = ?
        WHERE id = ?
    """, (status, int(time.time()), signal_id))

    conn.commit()
    conn.close()

    return True


# =========================
# CREATE NEW SIGNAL
# =========================
def create_signal(db_path, asset, entry, tp, sl, status="Upcoming"):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO signals (asset, entry, tp, sl, status)
        VALUES (?, ?, ?, ?, ?)
    """, (asset, entry, tp, sl, status))

    conn.commit()
    conn.close()


# =========================
# GET ALL SIGNALS
# =========================
def get_all_signals(db_path):

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    data = cur.execute("""
        SELECT *
        FROM signals
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    return data


# =========================
# GET ACTIVE SIGNALS ONLY
# =========================
def get_active_signals(db_path):

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    data = cur.execute("""
        SELECT *
        FROM signals
        WHERE status != 'Expired'
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    return data
