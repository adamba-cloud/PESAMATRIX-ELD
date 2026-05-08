import sqlite3
import os
from werkzeug.security import generate_password_hash


# =========================
# DATABASE PATH
# =========================
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATABASE = os.path.join(
    BASE_DIR,
    "database.db"
)


# =========================
# DB CONNECTION
# =========================
def get_db():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    conn.execute(
        "PRAGMA foreign_keys = ON"
    )

    return conn


# =========================
# INIT DATABASE
# =========================
def init_db():

    conn = get_db()

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

        telegram_id TEXT,

        created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP
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

        status TEXT,

        created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP
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
        DEFAULT 'Upcoming',

        created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # ================= CONTENT =================
    cur.execute("""

    CREATE TABLE IF NOT EXISTS content(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        type TEXT,

        title TEXT,

        link TEXT,

        created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # ================= FILES =================
    cur.execute("""

    CREATE TABLE IF NOT EXISTS files(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        filepath TEXT,

        type TEXT,

        uploaded_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # ================= LOGS =================
    cur.execute("""

    CREATE TABLE IF NOT EXISTS logs(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        action TEXT,

        user TEXT,

        time TEXT
        DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # ================= DEFAULT ADMIN =================
    admin_exists = cur.execute(
        """

        SELECT * FROM users
        WHERE role='admin'

        """
    ).fetchone()

    if not admin_exists:

        cur.execute(
            """

            INSERT INTO users
            (
                name,
                phone,
                email,
                password,
                role,
                status
            )

            VALUES (?, ?, ?, ?, ?, ?)

            """,
            (
                "Admin",
                "0700000000",
                "admin@pesamatrix.com",
                generate_password_hash(
                    "admin123"
                ),
                "admin",
                "active"
            )
        )

        print(
            "✅ Default admin created"
        )

    conn.commit()
    conn.close()

    print(
        "✅ Database initialized successfully"
    )
