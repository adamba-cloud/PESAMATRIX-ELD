from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

payments_bp = Blueprint("payments", __name__)

# temporary user store (replace later with DB)
users = {
    "test@gmail.com": {
        "role": "FREE"
    }
}


@payments_bp.route("/upgrade", methods=["POST"])
@jwt_required()
def upgrade_to_vip():

    email = get_jwt_identity()

    user = users.get(email)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    # simulate payment success
    user["role"] = "VIP"

    return jsonify({
        "message": "Payment successful. You are now VIP.",
        "role": user["role"]
    })
