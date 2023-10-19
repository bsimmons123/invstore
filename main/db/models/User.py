from werkzeug.security import check_password_hash

from main.db.database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    @property
    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True  # Implement your logic here

    def is_anonymous(self):
        return False

    def check_password(self, password):
        return check_password_hash(self.password, password)
