from enum import Enum

from flask import abort
from sqlalchemy.exc import IntegrityError, NoResultFound

from main.db.database import db
from main.db.models.Catering import CateringItem, CateringItemType, CateringList


class CateringErrorMsg(Enum):
    CATERING_LIST_TYPE_MISSING = "Name must not be empty"


def get_all_items():
    return CateringItem.query.all()


def get_item_by_id(item_id):
    return CateringItem.query.get(item_id)


def create_item(label, type_id, list_id):
    errors = []
    try:
        db.session.query(CateringItemType).filter_by(id=type_id).one()
    except NoResultFound:
        errors.append(f"CateringItemType with id {type_id} does not exist.")

    try:
        db.session.query(CateringList).filter_by(id=list_id).one()
    except NoResultFound:
        errors.append(f"CateringList with id {list_id} does not exist.")

    if errors:  # If there are any errors, return early
        return {"result": None, "errors": errors}

    item = CateringItem(label=label, type_id=type_id, list_id=list_id)
    try:
        db.session.add(item)
        db.session.commit()
        db.session.refresh(item)
    except IntegrityError:
        db.session.rollback()
        errors.append('There was an error adding the item to the database.')

    return {"result": item, "errors": errors}


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
