from flask import Blueprint, request, jsonify

from backend.services.auth_service import register_user, login_user
from backend.utils.jwt_helper import generate_token

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    register_user(
        data["name"],
        data["email"],
        data["password"]
    )

    return jsonify({"message": "User registered"})


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    user = login_user(data["email"], data["password"])

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(user["id"], user["role"])

    return jsonify({
        "token": token,
        "user": {
            "id": user["id"],
            "email": user["email"],
            "role": user["role"]
        }
    })
