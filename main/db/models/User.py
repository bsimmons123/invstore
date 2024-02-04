from datetime import datetime

from flask_login import current_user
from pytz import timezone, utc
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
    timezone = db.Column(db.String(50), default='UTC')

    def get_id(self):
        return str(self.id)

    @property
    def is_authenticated(self):
        return True if current_user.get_id() is not None else False

    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Convert timezones from UTC to local time zone for users
    @property
    def local_last_logged_in(self):
        return self.utc_to_local(self.last_logged_in)

    @property
    def local_created_at(self):
        return self.utc_to_local(self.created_at)

    @property
    def local_updated_at(self):
        return self.utc_to_local(self.updated_at)

    def utc_to_local(self, utc_dt):
        local_tz = timezone(self.timezone)
        local_dt = utc_dt.replace(tzinfo=utc).astimezone(local_tz)
        return local_tz.normalize(local_dt)  # .normalize might be necessary as not all days have the same duration (due to DST transitions, for example)


class UserList(db.Model):
    __tablename__ = 'user_list'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('c_list.id'), nullable=False)
    role = db.Column(db.String(50))  # Example role field
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
