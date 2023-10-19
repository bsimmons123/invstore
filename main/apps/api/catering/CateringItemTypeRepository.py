from main.db.database import db
from main.db.models.Catering import CateringItem, CateringItemType


def get_all_items():
    return CateringItemType.query.all()


def get_item_by_id(item_id):
    return CateringItemType.query.get(item_id)

def get_item_by_user_id(user_id):
    return CateringItemType.query.filter_by(user_id=user_id).all()


def create_item(label, user_id):
    item = CateringItemType(label=label, user_id=user_id)
    db.session.add(item)
    db.session.commit()
    return item


def update_item(item_id, name, type):
    item = CateringItemType.query.get(item_id)
    if item:
        item.name = name
        item.type = type
        db.session.commit()
    return item


def delete_item(item_id):
    item = CateringItemType.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return item
