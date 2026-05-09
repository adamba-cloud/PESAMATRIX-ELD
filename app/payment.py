from flask import Blueprint, jsonify
from utils.db import get_db

payments_bp = Blueprint("payments", __name__)

@payments_bp.route("/")
def payments():

    conn = get_db()
    rows = conn.execute("SELECT * FROM payments ORDER BY id DESC").fetchall()
    conn.close()

    return jsonify([dict(r) for r in rows])
