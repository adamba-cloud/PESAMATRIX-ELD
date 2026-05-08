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

# ================= ACCESS CODES (UPGRADED) =================
cur.execute("""

CREATE TABLE IF NOT EXISTS access_codes(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    code TEXT UNIQUE,

    status TEXT DEFAULT 'active',

    used INTEGER DEFAULT 0,

    used_at TIMESTAMP,

    expires_at TIMESTAMP,

    created_at TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id)
    ON DELETE CASCADE
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
