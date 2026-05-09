from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

users_bp = Blueprint("users", __name__)


@users_bp.route("/profile")
@jwt_required()
def profile():
    return jsonify({"message": "User profile"})
