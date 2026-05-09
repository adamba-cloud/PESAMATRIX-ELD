from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timedelta

from backend.utils.db import get_db

payments_bp = Blueprint("payments", __name__)


@payments_bp.route("/subscribe-vip", methods=["POST"])
@jwt_required()
def subscribe_vip():

    email = get_jwt_identity()
    conn = get_db()

    # get user
    user = conn.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    ).fetchone()

    if not user:
        return jsonify({"msg": "User not found"}), 404

    # check if already subscribed
    existing = conn.execute(
        "SELECT * FROM subscriptions WHERE user_id = ? AND status = 'active'",
        (user["id"],)
    ).fetchone()

    if existing:
        return jsonify({
            "message": "User already has an active subscription"
        }), 400

    # 30-day VIP subscription
    start_date = datetime.utcnow()
    end_date = start_date + timedelta(days=30)

    conn.execute(
        """
        INSERT INTO subscriptions (user_id, plan, status, start_date, end_date)
        VALUES (?, ?, ?, ?, ?)
        """,
        (user["id"], "VIP", "active", start_date, end_date)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "VIP subscription activated for 30 days",
        "plan": "VIP",
        "duration_days": 30
    })
