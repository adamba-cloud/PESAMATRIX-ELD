from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from backend.utils.db import get_db

auth_bp = Blueprint("auth", __name__)


# REGISTER
@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.json
    email = data.get("email")
    password = data.get("password")
    name = data.get("name", "User")

    conn = get_db()

    existing_user = conn.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    ).fetchone()

    if existing_user:
        return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(password)

    conn.execute(
        "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
        (name, email, hashed_password, "FREE")
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "User registered successfully"
    })


# LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json
    email = data.get("email")
    password = data.get("password")

    conn = get_db()

    user = conn.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    ).fetchone()

    conn.close()

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    if not check_password_hash(user["password"], password):
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(identity=email)

    return jsonify({
        "token": token,
        "role": user["role"]
    })
