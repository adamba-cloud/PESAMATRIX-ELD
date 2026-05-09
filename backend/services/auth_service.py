from werkzeug.security import generate_password_hash, check_password_hash
from backend.utils.db import get_db


def register_user(name, email, password):
    conn = get_db()

    hashed = generate_password_hash(password)

    conn.execute(
        "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
        (name, email, hashed, "user")
    )

    conn.commit()
    conn.close()


def login_user(email, password):
    conn = get_db()

    user = conn.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    ).fetchone()

    conn.close()

    if not user:
        return None

    if check_password_hash(user["password"], password):
        return user

    return None
