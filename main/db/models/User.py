from datetime import datetime
from werkzeug.security import check_password_hash

from main.db.database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(2000), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    last_logged_in = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

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

class UserList(db.Model):
    __tablename__ = 'user_list'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('c_list.id'), nullable=False)
    role = db.Column(db.String(50))  # Example role field
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
