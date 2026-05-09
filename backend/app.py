from flask import Flask
from flask_cors import CORS

from backend.config import Config
from backend.extensions import jwt, limiter

from backend.utils.db import init_db
from backend.utils.subscription_checker import expire_old_subscriptions

from backend.routes.auth import auth_bp
from backend.routes.admin import admin_bp
from backend.routes.users import users_bp
from backend.routes.signals import signals_bp
from backend.routes.payments import payments_bp
from backend.routes.subscriptions import subscriptions_bp


app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

jwt.init_app(app)
limiter.init_app(app)

# ✔ FIX: safe initialization context
with app.app_context():
    init_db(app)
    expire_old_subscriptions()   # NOW SAFE

# REGISTER BLUEPRINTS
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(admin_bp, url_prefix="/api/admin")
app.register_blueprint(users_bp, url_prefix="/api/users")
app.register_blueprint(signals_bp, url_prefix="/api/signals")
app.register_blueprint(payments_bp, url_prefix="/api/payments")
app.register_blueprint(subscriptions_bp, url_prefix="/api/subscriptions")


@app.route("/")
def home():
    return {"message": "Trading SaaS API Running"}


if __name__ == "__main__":
    app.run(debug=True)
