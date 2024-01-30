import os

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    # Assuming DATABASE_URL is defined in your environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Import your models here (after db is initialized)
    from main.db.models import User, Catering

    # Create tables (if they don't exist)
    with app.app_context():
        db.create_all()