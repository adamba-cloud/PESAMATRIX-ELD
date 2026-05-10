from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from backend.utils.db import get_db


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):

        # verify token exists
        verify_jwt_in_request()

        email = get_jwt_identity()

        conn = get_db()
        user = conn.execute(
            "SELECT role FROM users WHERE email = ?",
            (email,)
        ).fetchone()
        conn.close()

        if not user or user["role"] != "ADMIN":
            return jsonify({"message": "Admin access required"}), 403

        return fn(*args, **kwargs)

    return wrapper
