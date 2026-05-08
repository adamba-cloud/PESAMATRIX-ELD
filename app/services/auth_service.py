import hashlib
import random
from app.database import get_db


# =========================
# PASSWORD SECURITY
# =========================
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed


# =========================
# CREATE USER
# =========================
def create_user(name, phone, email, password):

    conn = get_db()
    cur = conn.cursor()

    try:
        account_number = str(random.randint(100000, 999999))

        cur.execute("""
            INSERT INTO users(
                name,
                phone,
                email,
                password,
                role,
                status,
                account_number
            )
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
        return account_number

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()


# =========================
# GET USER BY PHONE
# =========================
def get_user(phone):

    conn = get_db()
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE phone=?", (phone,))
    user = cur.fetchone()

    conn.close()
    return user


# =========================
# AUTHENTICATE USER
# =========================
def authenticate(phone, password):

    user = get_user(phone)

    if not user:
        return None

    if verify_password(password, user["password"]):
        return user

    return None


# =========================
# SAFE DICT CONVERTER (IMPORTANT FIX)
# =========================
def dict_factory(cursor, row):
    """Convert SQLite row to dictionary safely"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
