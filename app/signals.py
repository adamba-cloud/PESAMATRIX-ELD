from flask import Blueprint, jsonify
from utils.db import get_db

signals_bp = Blueprint("signals", __name__)

@signals_bp.route("/")
def signals():

    conn = get_db()
    rows = conn.execute("SELECT * FROM signals ORDER BY id DESC").fetchall()
    conn.close()

    return jsonify([dict(r) for r in rows])
