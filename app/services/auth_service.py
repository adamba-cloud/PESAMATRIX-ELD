import sqlite3
import hashlib
import random

# =========================
# PASSWORD SECURITY
# =========================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password, hashed):
    return hash_password(password) == hashed


# =========================
# CREATE USER
# =========================
def create_user(db, name, phone, email, password):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    account_number = str(random.randint(100000, 999999))

    cur.execute("""
        INSERT INTO users(name, phone, email, password, role, status, account_number)
        VALUES(?,?,?,?,?,?,?)
    """, (
        name,
        phone,
        email,
        hash_password(password),
        "user",
        "inactive",
        account_number
    ))

    conn.commit()
    conn.close()

    return account_number


# =========================
# GET USER
# =========================
def get_user(db, phone):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE phone=?", (phone,))
    user = cur.fetchone()

    conn.close()
    return user


# =========================
# LOGIN USER
# =========================
def authenticate(db, phone, password):
    user = get_user(db, phone)

    if not user:
        return None

    if verify_password(password, user["password"]):
        return user

    return None
