from flask import Blueprint, jsonify
from utils.db import get_db

users_bp = Blueprint("users", __name__)

@users_bp.route("/")
def users():

    conn = get_db()
    rows = conn.execute("SELECT * FROM users ORDER BY id DESC").fetchall()
    conn.close()

    return jsonify([dict(r) for r in rows])
