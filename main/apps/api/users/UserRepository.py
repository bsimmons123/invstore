import re
from datetime import datetime
from enum import Enum

from flask import abort
from werkzeug.security import generate_password_hash

from main.db.database import db
from main.db.models.User import User


class UserErrorMsg(Enum):
    EMPTY_NAME = "Name must not be empty"
    SHORT_PASSWORD = "Password must be at least 8 characters long"
    INVALID_EMAIL = "Must be a valid email format"
    EMPTY_TIMEZONE = "Timezone must not be empty"
    DUPLICATE_EMAIL = "Email already exists"


def get_all_users():
    return User.query.all()


def get_user_by_id(item_id):
    return User.query.get(item_id)


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()


def create_user(name, password, email):
    if not name:
        abort(400, description=UserErrorMsg.EMPTY_NAME.value)
    if not password or len(password) < 8:
        abort(400, description=UserErrorMsg.SHORT_PASSWORD.value)
    if not email or not is_valid_email(email):
        abort(400, description=UserErrorMsg.INVALID_EMAIL.value)

    # Generate a hashed version of the password
    hashed_password = generate_password_hash(password, method='scrypt')

    # Create a new user with the hashed password
    user = User(name=name, password=hashed_password, email=email)

    # Add the user to the session and commit
    db.session.add(user)
    db.session.commit()

    user = User.query.filter_by(email=email).first()

    return user


def update_user_login_date(user_id):
    user = User.query.get(user_id)
    user.last_logged_in = datetime.utcnow()
    db.session.commit()


def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return user


def is_valid_email(email):
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.fullmatch(email_regex, email) is not None
