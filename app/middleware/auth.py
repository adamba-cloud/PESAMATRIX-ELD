from functools import wraps
from flask import session, redirect, url_for, request


# =========================
# LOGIN REQUIRED
# =========================
def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        # Check if user is logged in
        if "user_id" not in session:
            return redirect(url_for("auth.login", next=request.path))

        return func(*args, **kwargs)

    return wrapper


# =========================
# ADMIN REQUIRED
# =========================
def admin_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        # Must be logged in first
        if "user_id" not in session:
            return redirect(url_for("auth.login", next=request.path))

        # Must be admin role
        if session.get("role") != "admin":
            return redirect(url_for("user.dashboard"))

        return func(*args, **kwargs)

    return wrapper


# =========================
# OPTIONAL: GUEST ONLY (LOGIN PAGE PROTECTION)
# =========================
def guest_only(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "user_id" in session:
            # If already logged in, redirect to dashboard
            return redirect(url_for("user.dashboard"))

        return func(*args, **kwargs)

    return wrapper
