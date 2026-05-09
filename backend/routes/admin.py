from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from backend.middleware.admin_required import admin_required
from backend.utils.db import get_db

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/dashboard")
@jwt_required()
@admin_required

def dashboard():

    conn = get_db()

    data = {
        "users": conn.execute("SELECT COUNT(*) FROM users").fetchone()[0],
        "payments": conn.execute("SELECT COUNT(*) FROM payments").fetchone()[0],
        "signals": conn.execute("SELECT COUNT(*) FROM signals").fetchone()[0],
        "subscriptions": conn.execute("SELECT COUNT(*) FROM subscriptions").fetchone()[0]
    }

    conn.close()

    return jsonify(data)
