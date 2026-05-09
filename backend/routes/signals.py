from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from backend.utils.helpers import signals

signals_bp = Blueprint("signals", __name__)


@signals_bp.route("/", methods=["GET"])
@jwt_required()
def get_signals():

    return jsonify({
        "signals": signals
    })
