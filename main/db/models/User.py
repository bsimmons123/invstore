from datetime import datetime

from main.db.database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    last_logged_in = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    oauth_provider = db.Column(db.String(50))  # Example field to store the OAuth provider (e.g., 'google', 'facebook')
    oauth_uid = db.Column(db.String(120), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    # Additional fields for OAuth-specific data
    oauth_access_token = db.Column(db.String(255))
    oauth_refresh_token = db.Column(db.String(255))


class UserList(db.Model):
    __tablename__ = 'user_list'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('c_list.id'), nullable=False)
    role = db.Column(db.String(50))  # Example role field
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)