import sqlite3
from datetime import datetime


# =========================
# CREATE LOG TABLE
# =========================
def create_log_table(db_path):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS logs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        action TEXT NOT NULL,     -- e.g login, payment, signal_update
        user TEXT,                -- phone or user id
        details TEXT,             -- extra info

        created_at TEXT DEFAULT (datetime('now'))

    )
    """)

    conn.commit()
    conn.close()


# =========================
# ADD LOG ENTRY
# =========================
def add_log(db_path, action, user, details=""):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO logs (action, user, details)
        VALUES (?, ?, ?)
    """, (action, user, details))

    conn.commit()
    conn.close()


# =========================
# GET ALL LOGS (ADMIN)
# =========================
def get_logs(db_path):

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    data = cur.execute("""
        SELECT *
        FROM logs
        ORDER BY id DESC
    """).fetchall()

    conn.close()
    return data


# =========================
# LOG USER LOGIN
# =========================
def log_login(db_path, phone):

    add_log(db_path, "login", phone, "User logged in")


# =========================
# LOG PAYMENT
# =========================
def log_payment(db_path, phone, amount):

    add_log(db_path, "payment", phone, f"Payment submitted: {amount}")


# =========================
# LOG SIGNAL UPDATE
# =========================
def log_signal_update(db_path, user, signal_id, status):

    add_log(
        db_path,
        "signal_update",
        user,
        f"Signal {signal_id} changed to {status}"
    )
