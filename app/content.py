from flask import Blueprint, jsonify
from utils.db import get_db

content_bp = Blueprint("content", __name__)

@content_bp.route("/")
def content():

    conn = get_db()
    rows = conn.execute("SELECT * FROM content ORDER BY id DESC").fetchall()
    conn.close()

    return jsonify([dict(r) for r in rows])
