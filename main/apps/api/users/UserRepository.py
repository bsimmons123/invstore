from werkzeug.security import generate_password_hash

from main.db.database import db
from main.db.models.User import User


def get_all_users():
    return User.query.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def create_user(id, name, email):
    # Create a new user
    user = User(id=id, name=name, email=email)

    # Add the user to the session and commit
    db.session.add(user)
    db.session.commit()

    user = User.query.filter_by(email=email).first()

    return user


def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return user
