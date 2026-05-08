from functools import wraps
from flask import session, redirect, url_for


# =========================
# ADMIN DECORATOR
# =========================
def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        # check login
        if "user_id" not in session:
            return redirect(url_for("auth.login"))

        # check role
        if session.get("role") != "admin":
            return redirect(url_for("user.dashboard"))

        return func(*args, **kwargs)

    return wrapper


# =========================
# LOGIN REQUIRED DECORATOR
# =========================
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:
            return redirect(url_for("auth.login"))

        return func(*args, **kwargs)

    return wrapper
