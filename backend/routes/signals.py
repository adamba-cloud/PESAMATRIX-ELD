from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from backend.utils.db import get_db
from backend.middleware.subscription_required import subscription_required

signals_bp = Blueprint("signals", __name__)


# =========================
# CREATE SIGNAL (ADMIN ONLY)
# =========================
@signals_bp.route("/create", methods=["POST"])
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
            data["pair"],
            data["type"],
            data["entry"],
            data["tp"],
            data["sl"]
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Signal created"})


# =========================
# FREE SIGNALS (LIMITED)
# =========================
@signals_bp.route("/", methods=["GET"])
@jwt_required()
def get_signals():

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM signals ORDER BY id DESC LIMIT 2"
    ).fetchall()

    conn.close()

    return jsonify({
        "signals": [dict(row) for row in rows]
    })


# =========================
# VIP SIGNALS (FULL ACCESS)
# =========================
@signals_bp.route("/vip", methods=["GET"])
@subscription_required
def get_vip_signals():

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM signals ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return jsonify({
        "signals": [dict(row) for row in rows]
    })
