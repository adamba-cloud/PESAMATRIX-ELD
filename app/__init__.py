from flask import Flask
from app.config import Config
import os

def create_app():
    app = Flask(__name__)

    # =========================
    # CONFIG
    # =========================
    app.config.from_object(Config)

    # =========================
    # CREATE REQUIRED FOLDERS
    # =========================
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # =========================
    # REGISTER BLUEPRINTS
    # =========================

    from app.routes.landing import landing_bp
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.user import user_bp
    from app.routes.signals import signals_bp
    from app.routes.payments import payments_bp
    from app.routes.content import content_bp

    # =========================
    # LANDING PAGE (HOME)
    # =========================
    app.register_blueprint(landing_bp)

    # =========================
    # AUTH SYSTEM
    # =========================
    app.register_blueprint(auth_bp)

    # =========================
    # ADMIN PANEL
    # =========================
    app.register_blueprint(admin_bp)

    # =========================
    # USER PANEL
    # =========================
    app.register_blueprint(user_bp)

    # =========================
    # SIGNALS
    # =========================
    app.register_blueprint(signals_bp)

    # =========================
    # PAYMENTS
    # =========================
    app.register_blueprint(payments_bp)

    # =========================
    # CONTENT SYSTEM
    # =========================
    app.register_blueprint(content_bp)

    return app
