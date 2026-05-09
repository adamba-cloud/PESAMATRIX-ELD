from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

signals_bp = Blueprint("signals", __name__)

# temporary fake signals database
signals = [
    {
        "pair": "XAUUSD",
        "type": "BUY",
        "entry": 3320,
        "tp": 3350,
        "sl": 3300
    },
    {
        "pair": "EURUSD",
        "type": "SELL",
        "entry": 1.1200,
        "tp": 1.1100,
        "sl": 1.1250
    },
    {
        "pair": "BTCUSDT",
        "type": "BUY",
        "entry": 95000,
        "tp": 98000,
        "sl": 93000
    }
]

@signals_bp.route("/", methods=["GET"])
@jwt_required()
def get_signals():

    return jsonify({
        "signals": signals
    })
