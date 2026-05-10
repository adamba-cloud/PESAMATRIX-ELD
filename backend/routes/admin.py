from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from backend.utils.db import get_db
from backend.middleware.admin_required import admin_required

admin_bp = Blueprint("admin", __name__)


# =========================
# ADMIN DASHBOARD ANALYTICS (SECURED)
# =========================
@admin_bp.route("/analytics", methods=["GET"])
@jwt_required()
@admin_required
def admin_analytics():

    conn = get_db()

    total_users = conn.execute(
        "SELECT COUNT(*) as count FROM users"
    ).fetchone()["count"]

    vip_users = conn.execute(
        "SELECT COUNT(*) as count FROM users WHERE role = 'VIP'"
    ).fetchone()["count"]

    total_signals = conn.execute(
        "SELECT COUNT(*) as count FROM signals"
    ).fetchone()["count"]

    revenue = conn.execute(
        "SELECT COALESCE(SUM(amount), 0) as total FROM payments WHERE status = 'success'"
    ).fetchone()["total"]

    active_subs = conn.execute(
        "SELECT COUNT(*) as count FROM subscriptions WHERE status = 'active'"
    ).fetchone()["count"]

    conn.close()

    return jsonify({
        "total_users": total_users,
        "vip_users": vip_users,
        "total_signals": total_signals,
        "revenue": revenue,
        "active_subscriptions": active_subs
    })


# =========================
# CREATE SIGNAL (ADMIN ONLY)
# =========================
@admin_bp.route("/create-signal", methods=["POST"])
@jwt_required()
@admin_required
def create_signal():

    data = request.json

    if not data:
        return jsonify({"message": "Missing request data"}), 400

    conn = get_db()

    conn.execute(
        """
        INSERT INTO signals (pair, type, entry, tp, sl)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            data.get("pair"),
            data.get("type"),
            data.get("entry"),
            data.get("tp"),
            data.get("sl")
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Signal created successfully"
    }), 201
