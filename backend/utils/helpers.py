from datetime import datetime

# shared signals storage
signals = []


def now():
    return datetime.utcnow().isoformat()
