import hashlib
import random
from app.database import get_db

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
def create_user(name, phone, email, password):

    conn = get_db()
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
def get_user(phone):

    conn = get_db()
    conn.row_factory = None   # ❌ REMOVE THIS LINE
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE phone=?", (phone,))
    user = cur.fetchone()

    conn.close()
    return user


# =========================
# LOGIN USER
# =========================
def authenticate(phone, password):

    user = get_user(phone)

    if not user:
        return None

    # FIX: convert tuple → dict-safe handling depends on DB config
    if verify_password(password, user[4]):  # password column index
        return user

    return None
