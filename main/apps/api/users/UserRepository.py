from werkzeug.security import generate_password_hash

from main.db.database import db
from main.db.models.User import User


def get_all_users():
    return User.query.all()


def get_user_by_id(item_id):
    return User.query.get(item_id)


def create_user(name, password, email):
    # Generate a hashed version of the password
    hashed_password = generate_password_hash(password, method='sha256')

    # Create a new user with the hashed password
    user = User(name=name, password=hashed_password, email=email)

    # Add the user to the session and commit
    db.session.add(user)
    db.session.commit()

    return user


def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return user
