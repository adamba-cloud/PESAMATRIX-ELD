from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.utils.db import get_db

admin_bp = Blueprint("admin", __name__)


# =========================
# ADMIN DASHBOARD ANALYTICS
# =========================
@admin_bp.route("/analytics", methods=["GET"])
@jwt_required()
def admin_analytics():

    conn = get_db()

    # TOTAL USERS
    total_users = conn.execute(
        "SELECT COUNT(*) as count FROM users"
    ).fetchone()["count"]

    # TOTAL VIP USERS
    vip_users = conn.execute(
        "SELECT COUNT(*) as count FROM users WHERE role = 'VIP'"
    ).fetchone()["count"]

    # TOTAL SIGNALS
    total_signals = conn.execute(
        "SELECT COUNT(*) as count FROM signals"
    ).fetchone()["count"]

    # TOTAL REVENUE
    revenue = conn.execute(
        "SELECT COALESCE(SUM(amount), 0) as total FROM payments WHERE status = 'success'"
    ).fetchone()["total"]

    # ACTIVE SUBSCRIPTIONS
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
# CREATE SIGNAL (ADMIN)
# =========================
@admin_bp.route("/create-signal", methods=["POST"])
@jwt_required()
def create_signal():

    data = request.json

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
    })
