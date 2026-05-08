from flask import session, redirect

def admin_required():
    if session.get("role") != "admin":
        return False
    return True
