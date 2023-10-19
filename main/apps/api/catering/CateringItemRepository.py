from main.db.database import db
from main.db.models.Catering import CateringItem


def get_all_items():
    return CateringItem.query.all()


def get_item_by_id(item_id):
    return CateringItem.query.get(item_id)


def create_item(label, type_id, list_id):
    item = CateringItem(label=label, type_id=type_id, list_id=list_id)
    db.session.add(item)
    db.session.commit()
    return item


def update_item(item_id, name, type):
    item = CateringItem.query.get(item_id)
    if item:
        item.name = name
        item.type = type
        db.session.commit()
    return item


def delete_item(item_id):
    item = CateringItem.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return item
