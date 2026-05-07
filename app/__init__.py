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

    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.user import user_bp
    from app.routes.signals import signals_bp
    from app.routes.payments import payments_bp
    from app.routes.content import content_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)

    # signals
    app.register_blueprint(signals_bp)

    # payments (✔ THIS IS CORRECT)
    app.register_blueprint(payments_bp)

    # content
    app.register_blueprint(content_bp)

    # =========================
    # HOME ROUTE
    # =========================
    @app.route("/")
    def home():
        return """
        <h1 style='text-align:center;font-family:Arial'>
        PESAMATRIX PRO SaaS Running 🚀
        </h1>
        <p style='text-align:center'>System is active</p>
        """

    return app
