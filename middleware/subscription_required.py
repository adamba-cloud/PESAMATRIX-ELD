from functools import wraps
from flask import jsonify


def subscription_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper
