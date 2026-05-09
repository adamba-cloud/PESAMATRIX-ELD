from flask import Blueprint, jsonify

user_bp = Blueprint("user", __name__)

@user_bp.route("/dashboard")
def dashboard():

    return jsonify({
        "user": {
            "name": "Demo User",
            "plan": "Premium"
        },
        "stats": {
            "signals": 12,
            "content": 4
        }
    })
