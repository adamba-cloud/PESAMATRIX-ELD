from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    email = data.get("email")
    password = data.get("password")

    # demo logic (replace with DB)
    if email == "admin@saas.com" and password == "1234":

        return jsonify({
            "token": "demo-token",
            "role": "admin",
            "user_id": 1
        })

    return jsonify({"error": "Invalid login"}), 401
