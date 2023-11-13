from main.db.database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(500), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
