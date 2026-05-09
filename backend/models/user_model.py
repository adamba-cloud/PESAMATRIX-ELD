from datetime import datetime


class User:
    def __init__(self, id, name, email, password, role="FREE"):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.created_at = datetime.utcnow()
