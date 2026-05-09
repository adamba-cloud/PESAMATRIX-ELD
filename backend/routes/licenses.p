from flask import Blueprint, jsonify
from utils.db import get_db

licenses_bp = Blueprint("licenses", __name__)

@licenses_bp.route("/")
def licenses():

    conn = get_db()
    rows = conn.execute("SELECT * FROM licenses ORDER BY id DESC").fetchall()
    conn.close()

    return jsonify([dict(r) for r in rows])
