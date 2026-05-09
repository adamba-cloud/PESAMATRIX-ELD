from flask import Blueprint, jsonify
from backend.utils.db import get_db

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/dashboard")
def dashboard():

    conn = get_db()

    data = {
        "users": conn.execute("SELECT COUNT(*) FROM users").fetchone()[0],
        "payments": conn.execute("SELECT COUNT(*) FROM payments").fetchone()[0],
        "signals": conn.execute("SELECT COUNT(*) FROM signals").fetchone()[0],
        "content": conn.execute("SELECT COUNT(*) FROM content").fetchone()[0],
        "licenses": conn.execute("SELECT COUNT(*) FROM licenses").fetchone()[0],
        "logs": conn.execute("SELECT COUNT(*) FROM audit_logs").fetchone()[0],
    }

    conn.close()
    return jsonify(data)
