from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from backend.utils.helpers import signals
from backend.middleware.subscription_required import subscription_required

signals_bp = Blueprint("signals", __name__)


# FREE SIGNALS (all users)
@signals_bp.route("/", methods=["GET"])
@jwt_required()
def get_signals():

    return jsonify({
        "signals": signals[:2]  # free users see limited signals
    })


# VIP / SUBSCRIPTION SIGNALS (paid users only)
@signals_bp.route("/vip", methods=["GET"])
@subscription_required
def get_vip_signals():

    return jsonify({
        "signals": signals  # full access
    })
