from datetime import datetime

from werkzeug.security import generate_password_hash

from main.db.database import db
from main.db.models.User import User


def get_all_users():
    return User.query.all()


def get_user_by_id(item_id):
    return User.query.get(item_id)


def create_user(name, password, email, timezone):
    # Generate a hashed version of the password
    hashed_password = generate_password_hash(password, method='scrypt')

    # Create a new user with the hashed password
    user = User(name=name, password=hashed_password, email=email, timezone=timezone)

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
