import sqlite3
from flask import g
import os

DATABASE = os.path.join(os.path.dirname(__file__), "../database/trading_saas.db")


def get_db():
    db = getattr(g, "_database", None)

    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row

    return db


def init_db(app):
    with app.app_context():
        db = get_db()

        with open("backend/database/schema.sql", "r") as f:
            db.executescript(f.read())

        db.commit()
