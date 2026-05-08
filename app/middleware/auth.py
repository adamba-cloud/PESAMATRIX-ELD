from functools import wraps
from flask import session, redirect, url_for, request


# =========================
# LOGIN REQUIRED
# =========================
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:
            return redirect(url_for("auth.login"))

        return f(*args, **kwargs)

    return wrapper


# =========================
# ADMIN REQUIRED
# =========================
def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:
            return redirect(url_for("auth.login"))

        if session.get("role") != "admin":
            return redirect(url_for("user.dashboard"))

        return f(*args, **kwargs)

    return wrapper
