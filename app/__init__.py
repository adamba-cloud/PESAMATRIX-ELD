from flask import Flask
import os

def create_app():

    app = Flask(__name__)

    # =========================
    # BASIC CONFIG (RENDER SAFE)
    # =========================
    app.secret_key = os.environ.get("SECRET_KEY", "secret123")

    app.config["DATABASE"] = os.environ.get("DATABASE", "database.db")
    app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "static/uploads")

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

    app.register_blueprint(landing_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(signals_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(content_bp)

    return app
