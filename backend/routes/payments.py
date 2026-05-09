from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.utils.db import get_db

payments_bp = Blueprint("payments", __name__)


@payments_bp.route("/upgrade", methods=["POST"])
@jwt_required()
def upgrade_to_vip():

    email = get_jwt_identity()

    conn = get_db()

    user = conn.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    ).fetchone()

    if not user:
        return jsonify({"msg": "User not found"}), 404

    conn.execute(
        "UPDATE users SET role = 'VIP' WHERE email = ?",
        (email,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Payment successful. You are now VIP.",
        "role": "VIP"
    })
