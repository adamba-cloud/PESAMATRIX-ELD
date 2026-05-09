from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from backend.utils.helpers import signals
from backend.middleware.vip_required import vip_required

signals_bp = Blueprint("signals", __name__)


# FREE SIGNALS (all users)
@signals_bp.route("/", methods=["GET"])
@jwt_required()
def get_signals():

    return jsonify({
        "signals": signals[:2]  # free users see limited signals
    })


# VIP SIGNALS (premium users only)
@signals_bp.route("/vip", methods=["GET"])
@vip_required
def get_vip_signals():

    return jsonify({
        "signals": signals  # full access
    })
