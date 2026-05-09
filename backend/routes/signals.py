from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from backend.utils.db import get_db

signals_bp = Blueprint("signals", __name__)


@signals_bp.route("/create", methods=["POST"])
@jwt_required()
def create_signal():

    data = request.json

    conn = get_db()

    conn.execute(
        "INSERT INTO signals (pair, entry, stop_loss, take_profit) VALUES (?, ?, ?, ?)",
        (
            data["pair"],
            data["entry"],
            data["stop_loss"],
            data["take_profit"]
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Signal created"})


@signals_bp.route("/list")
@jwt_required()
def list_signals():

    conn = get_db()

    signals = conn.execute("SELECT * FROM signals").fetchall()

    conn.close()

    return jsonify([dict(x) for x in signals])
