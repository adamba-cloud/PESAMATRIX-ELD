from functools import wraps
from flask import session, redirect, url_for


# =========================
# LOGIN REQUIRED
# =========================
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("user_id"):
            return redirect(url_for("auth.login"))
        return func(*args, **kwargs)
    return wrapper


# =========================
# ADMIN REQUIRED (SECURE)
# =========================
def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if not session.get("user_id"):
            return redirect(url_for("auth.login"))

        if session.get("role") != "admin":
            return redirect(url_for("user.dashboard"))

        return func(*args, **kwargs)

    return wrapper
