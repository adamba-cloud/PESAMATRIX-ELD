import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify, current_app


# =========================
# CREATE JWT TOKEN
# =========================
def create_token(user_id, role):

    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }

    token = jwt.encode(
        payload,
        current_app.config["JWT_SECRET"],
        algorithm=current_app.config["JWT_ALGORITHM"]
    )

    return token


# =========================
# DECODE TOKEN
# =========================
def decode_token(token):

    try:
        return jwt.decode(
            token,
            current_app.config["JWT_SECRET"],
            algorithms=[current_app.config["JWT_ALGORITHM"]]
        )

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None


# =========================
# LOGIN REQUIRED DECORATOR
# =========================
def login_required(f):

    @wraps(f)
    def wrapper(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Missing token"}), 401

        # Expect: Bearer TOKEN
        try:
            token = token.split(" ")[1]
        except:
            return jsonify({"error": "Invalid token format"}), 401

        data = decode_token(token)

        if not data:
            return jsonify({"error": "Invalid or expired token"}), 401

        request.user = data
        return f(*args, **kwargs)

    return wrapper


# =========================
# ADMIN ONLY DECORATOR
# =========================
def admin_required(f):

    @wraps(f)
    def wrapper(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Missing token"}), 401

        try:
            token = token.split(" ")[1]
        except:
            return jsonify({"error": "Invalid token format"}), 401

        data = decode_token(token)

        if not data:
            return jsonify({"error": "Invalid token"}), 401

        if data.get("role") != "admin":
            return jsonify({"error": "Admin access required"}), 403

        request.user = data
        return f(*args, **kwargs)

    return wrapper
