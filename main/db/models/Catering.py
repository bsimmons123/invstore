from datetime import datetime
from sqlalchemy import CheckConstraint
from main.db.database import db


class CateringItem(db.Model):
    __tablename__ = 'c_item'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(500))
    type_id = db.Column(db.Integer, db.ForeignKey('c_item_type.id'))
    list_id = db.Column(db.Integer, db.ForeignKey('c_list.id'))
    description = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    quantity = db.Column(db.Integer, default=1)
    status = db.Column(db.String(20), CheckConstraint("status IN ('pending', 'confirmed', 'delivered')"))

    type = db.relationship('CateringItemType', backref='c_item_type')
    list = db.relationship('CateringList', backref='c', viewonly=True)

    def __repr__(self):
        return f"<CateringItem(label={self.label}, description={self.description}, status={self.status}, created_at={self.created_at}, updated_at={self.updated_at})>"


class CateringList(db.Model):
    __tablename__ = 'c_list'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.String(500))
    max_users = db.Column(db.Integer)
    session_id = db.Column(db.String(10), nullable=False)
    item_limit = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    location = db.Column(db.String(200))
    visibility = db.Column(db.String(20), CheckConstraint("visibility IN ('public', 'private', 'invite_only')"))

    # Define a relationships
    user = db.relationship('User', backref='user')
    c_items = db.relationship('CateringItem', backref='c_items')

    def __repr__(self):
        return f"<CateringList(label={self.label}, user_id={self.user_id}, description={self.description}, max_users={self.max_users}, session_id={self.session_id}, item_limit={self.item_limit}, created_at={self.created_at}, updated_at={self.updated_at}, is_active={self.is_active}, location={self.location}, visibility={self.visibility})>"


class CateringItemType(db.Model):
    __tablename__ = 'c_item_type'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(500))
    list_id = db.Column(db.Integer, db.ForeignKey('c_list.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # Define a relationship to the CateringList model
    list = db.relationship('CateringList', backref='catering_item_type')

    def __repr__(self):
        return f"<CateringItemType(label={self.label}, list_id={self.list_id})>"


class InviteList(db.Model):
    __tablename__ = 'invite_list'

    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    who_invited_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('c_list.id'), nullable=False)
    accepted = db.Column(db.Boolean, default=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    who_invited = db.relationship('User', backref='invitations_sent', foreign_keys=[who_invited_id])
    related_list = db.relationship('CateringList', backref='invitations')

    def __repr__(self):
        return f"<InviteList(user_email={self.user_email}, list_id={self.list_id}, accepted={self.accepted}, date_sent={self.date_sent})>"
