from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from backend.utils.db import get_db

payments_bp = Blueprint("payments", __name__)


@payments_bp.route("/submit", methods=["POST"])
@jwt_required()
def submit_payment():

    data = request.json

    conn = get_db()

    conn.execute(
        "INSERT INTO payments (user_id, amount, mpesa_code, status) VALUES (?, ?, ?, ?)",
        (
            data["user_id"],
            data["amount"],
            data["mpesa_code"],
            "pending"
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Payment submitted"})
