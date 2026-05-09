from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

# temporary user store (replace later with DB)
users = {
    "test@gmail.com": {
        "role": "VIP"
    }
}

def vip_required(fn):

    def wrapper(*args, **kwargs):

        verify_jwt_in_request()

        user_email = get_jwt_identity()

        user = users.get(user_email)

        if not user:
            return jsonify({"msg": "User not found"}), 404

        if user["role"] != "VIP":
            return jsonify({"msg": "VIP access required"}), 403

        return fn(*args, **kwargs)

    wrapper.__name__ = fn.__name__
    return wrapper
