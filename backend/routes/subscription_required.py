from flask import Blueprint, jsonify

subscriptions_bp = Blueprint("subscriptions", __name__)


@subscriptions_bp.route("/plans")
def plans():
    return jsonify([
        {"name": "Free", "price": 0},
        {"name": "VIP", "price": 50}
    ])
