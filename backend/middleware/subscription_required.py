from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from backend.utils.db import get_db


def subscription_required(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):

        verify_jwt_in_request()

        email = get_jwt_identity()
        conn = get_db()

        user = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        if not user:
            return jsonify({"msg": "User not found"}), 404

        subscription = conn.execute(
            "SELECT * FROM subscriptions WHERE user_id = ? AND status = 'active'",
            (user["id"],)
        ).fetchone()

        if not subscription:
            return jsonify({"msg": "Active subscription required"}), 403

        return fn(*args, **kwargs)

    return wrapper
