import sqlite3
import os

# =========================
# DATABASE PATH (RENDER SAFE)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.db")


# =========================
# DATABASE CONNECTION
# =========================
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row   # ✔ ensures dict-like access
    return conn


# =========================
# INITIALIZE DATABASE
# =========================
def init_db():

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    # ================= USERS =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT UNIQUE,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT DEFAULT 'user',
        status TEXT DEFAULT 'inactive',
        account_number TEXT,
        telegram_id TEXT
    )
    """)

    # ================= PAYMENTS =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT,
        mpesa_code TEXT,
        amount TEXT,
        plan TEXT,
        status TEXT
    )
    """)

    # ================= SIGNALS =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS signals(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset TEXT,
        entry TEXT,
        tp TEXT,
        sl TEXT,
        status TEXT
    )
    """)

    # ================= CONTENT =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS content(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        title TEXT,
        link TEXT
    )
    """)

    conn.commit()
    conn.close()
