from flask import Blueprint, jsonify
from utils.db import get_db

audit_bp = Blueprint("audit", __name__)

@audit_bp.route("/")
def logs():

    conn = get_db()
    rows = conn.execute("SELECT * FROM audit_logs ORDER BY id DESC").fetchall()
    conn.close()

    return jsonify([dict(r) for r in rows])
