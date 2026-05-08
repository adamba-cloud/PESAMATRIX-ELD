from flask import session

def admin_required():

    return (
        session.get("user_id") is not None
        and session.get("role") == "admin"
    )
