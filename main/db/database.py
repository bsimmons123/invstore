from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)

    # Import your models here (after db is initialized)
    from main.db.models import Catering, User

    # Create tables (if they don't exist)
    with app.app_context():
        db.create_all()
