from main.db.database import db


class CateringItem(db.Model):
    __tablename__ = 'catering_item'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(500))
    type_id = db.Column(db.Integer, db.ForeignKey('catering_item_type.id'))
    list_id = db.Column(db.Integer, db.ForeignKey('catering_list.id'))

    type = db.relationship('CateringItemType', backref='catering_item_type')
    list = db.relationship('CateringList', backref='catering_list', viewonly=True)


class CateringList(db.Model):
    __tablename__ = 'catering_list'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(500))
    user_id = db.Column(db.String(500), db.ForeignKey('user.id'))

    # Define a relationships
    user = db.relationship('User', backref='user')
    catering_items = db.relationship('CateringItem', backref='catering_items')


class CateringItemType(db.Model):
    __tablename__ = 'catering_item_type'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(500))
    user_id = db.Column(db.String(500), db.ForeignKey('user.id'))

    # Define a relationship to the User model
    user = db.relationship('User', backref='catering_item_type')
