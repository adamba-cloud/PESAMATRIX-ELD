import os
from datetime import timedelta


class Config:

    # =========================
    # SECURITY
    # =========================
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")
    JWT_SECRET = os.getenv("JWT_SECRET", "change-this-jwt-secret")

    # =========================
    # DATABASE
    # =========================
    DATABASE = os.getenv("DATABASE_URL", "database.db")

    # =========================
    # JWT SETTINGS
    # =========================
    JWT_ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_DAYS = 7

    # =========================
    # SESSION (optional fallback)
    # =========================
    SESSION_PERMANENT = False
