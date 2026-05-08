import sqlite3


# =========================
# CREATE CONTENT TABLE
# =========================
def create_content_table(db_path):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS content (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        type TEXT NOT NULL,          -- image, video, news, link

        title TEXT NOT NULL,

        link TEXT NOT NULL,          -- file path or external URL

        uploaded_by TEXT,            -- admin/user identifier

        status TEXT DEFAULT 'active', -- active/hidden

        created_at TEXT DEFAULT (datetime('now')),

        updated_at TEXT DEFAULT (datetime('now'))

    )
    """)

    conn.commit()
    conn.close()


# =========================
# INSERT CONTENT
# =========================
def create_content(db_path, content_type, title, link, uploaded_by="admin"):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO content (
            type, title, link, uploaded_by
        )
        VALUES (?, ?, ?, ?)
    """, (content_type, title, link, uploaded_by))

    conn.commit()
    conn.close()


# =========================
# GET ALL CONTENT
# =========================
def get_all_content(db_path):

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    data = cur.execute("""
        SELECT *
        FROM content
        WHERE status = 'active'
        ORDER BY id DESC
    """).fetchall()

    conn.close()
    return data


# =========================
# FILTER BY TYPE
# =========================
def get_content_by_type(db_path, content_type):

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    data = cur.execute("""
        SELECT *
        FROM content
        WHERE type = ?
        AND status = 'active'
        ORDER BY id DESC
    """, (content_type,)).fetchall()

    conn.close()
    return data


# =========================
# UPDATE CONTENT STATUS (ADMIN)
# =========================
def update_content_status(db_path, content_id, status):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        UPDATE content
        SET status = ?,
            updated_at = datetime('now')
        WHERE id = ?
    """, (status, content_id))

    conn.commit()
    conn.close()


# =========================
# DELETE CONTENT
# =========================
def delete_content(db_path, content_id):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM content
        WHERE id = ?
    """, (content_id,))

    conn.commit()
    conn.close()
