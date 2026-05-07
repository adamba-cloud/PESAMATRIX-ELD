import sqlite3
from app.config import Config

# =========================
# DATABASE CONNECTION
# =========================
def get_db():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# INITIALIZE DATABASE
# =========================
def init_db():
    conn = sqlite3.connect(Config.DATABASE)
    cur = conn.cursor()

    # ================= USERS =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT,
        email TEXT,
        password TEXT,
        role TEXT,
        status TEXT DEFAULT 'inactive',
        account_number TEXT,
        telegram_id TEXT
    )
    """)

    # ================= PAYMENTS =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments(
        id INTEGER PRIMARY KEY,
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
        id INTEGER PRIMARY KEY,
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
        id INTEGER PRIMARY KEY,
        type TEXT,
        title TEXT,
        link TEXT
    )
    """)

    conn.commit()
    conn.close()

    # 🔥 AFTER TABLE CREATION → SAFELY ADD COLUMN
    add_telegram_column()


# =========================
# SAFE COLUMN ADDITION
# =========================
def add_telegram_column():
    conn = sqlite3.connect(Config.DATABASE)
    cur = conn.cursor()

    try:
        cur.execute("ALTER TABLE users ADD COLUMN telegram_id TEXT")
        conn.commit()
    except:
        # column already exists → ignore safely
        pass

    conn.close()


# =========================
# AUTO RUN ON STARTUP
# =========================
init_db()
