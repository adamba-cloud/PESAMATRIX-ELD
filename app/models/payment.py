import sqlite3
from datetime import datetime


# =========================
# CREATE PAYMENT TABLE
# =========================
def create_payment_table(db_path):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        phone TEXT NOT NULL,

        mpesa_code TEXT UNIQUE,   -- prevents duplicate submissions

        amount TEXT NOT NULL,

        plan TEXT NOT NULL,

        status TEXT DEFAULT 'pending',

        created_at TEXT DEFAULT (datetime('now')),
        approved_at TEXT

    )
    """)

    conn.commit()
    conn.close()


# =========================
# CREATE PAYMENT RECORD
# =========================
def create_payment(db_path, phone, mpesa_code, amount, plan):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO payments (
                phone, mpesa_code, amount, plan, status
            )
            VALUES (?, ?, ?, ?, 'pending')
        """, (phone, mpesa_code, amount, plan))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        # duplicate mpesa code
        return False

    finally:
        conn.close()


# =========================
# APPROVE PAYMENT (ADMIN)
# =========================
def approve_payment(db_path, payment_id):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        UPDATE payments
        SET status = 'approved',
            approved_at = datetime('now')
        WHERE id = ?
    """, (payment_id,))

    conn.commit()
    conn.close()


# =========================
# GET USER PAYMENTS
# =========================
def get_user_payments(db_path, phone):

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    data = cur.execute("""
        SELECT *
        FROM payments
        WHERE phone = ?
        ORDER BY id DESC
    """, (phone,)).fetchall()

    conn.close()
    return data


# =========================
# GET ALL PAYMENTS (ADMIN)
# =========================
def get_all_payments(db_path):

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    data = cur.execute("""
        SELECT *
        FROM payments
        ORDER BY id DESC
    """).fetchall()

    conn.close()
    return data


# =========================
# CHECK PAYMENT STATUS
# =========================
def is_payment_approved(db_path, phone):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    result = cur.execute("""
        SELECT COUNT(*)
        FROM payments
        WHERE phone = ? AND status = 'approved'
    """, (phone,)).fetchone()[0]

    conn.close()

    return result > 0
