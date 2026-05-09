from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

admin_bp = Blueprint("admin", __name__)

# shared temporary signals database
signals = []

@admin_bp.route("/create-signal", methods=["POST"])
@jwt_required()
def create_signal():

    data = request.json

    signal = {
        "pair": data.get("pair"),
        "type": data.get("type"),
        "entry": data.get("entry"),
        "tp": data.get("tp"),
        "sl": data.get("sl")
    }

    signals.append(signal)

    return jsonify({
        "message": "Signal created successfully",
        "signal": signal
    })
