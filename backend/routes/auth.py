from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

# temporary fake database
users = []

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.json

    email = data.get("email")
    password = data.get("password")

    # check existing
    for user in users:
        if user["email"] == email:
            return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(password)

    users.append({
        "email": email,
        "password": hashed_password
    })

    return jsonify({
        "message": "User registered successfully"
    })


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    email = data.get("email")
    password = data.get("password")

    for user in users:

        if user["email"] == email:

            if check_password_hash(user["password"], password):

                token = create_access_token(identity=email)

                return jsonify({
                    "token": token
                })

    return jsonify({
        "message": "Invalid credentials"
    }), 401
