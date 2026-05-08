from functools import wraps
from flask import session, redirect

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        # check login
        if "user_id" not in session:
            return redirect("/login")

        # check admin role
        if session.get("role") != "admin":
            return redirect("/")

        return f(*args, **kwargs)

    return wrapper
