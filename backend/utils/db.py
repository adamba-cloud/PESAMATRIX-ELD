import sqlite3
from flask import current_app, g

# =========================
# GET DATABASE CONNECTION
# =========================
def get_db():

    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"]
        )
        g.db.row_factory = sqlite3.Row

    return g.db


# =========================
# CLOSE DB CONNECTION
# =========================
def close_db(e=None):

    db = g.pop("db", None)

    if db is not None:
        db.close()
