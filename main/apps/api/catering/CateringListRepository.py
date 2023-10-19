from main.db.database import db
from main.db.models.Catering import CateringList


def get_all_lists():
    return CateringList.query.all()


def get_all_lists_from_user(user_id):
    return CateringList.query.filter_by(user_id=user_id).all()


def get_list_by_id(id):
    return CateringList.query.get(id)


def create_list(label, user_id):
    list = CateringList(label=label, user_id=user_id)
    db.session.add(list)
    db.session.commit()
    return list


def update_list(list_id, name, type):
    item = CateringList.query.get(list_id)
    if item:
        item.name = name
        item.type = type
        db.session.commit()
    return item


def delete_list(item_id):
    item = CateringList.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return item
