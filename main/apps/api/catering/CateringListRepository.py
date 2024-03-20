from sqlalchemy.exc import NoResultFound, IntegrityError

from main.db.database import db
from main.db.models.Catering import CateringList
from main.db.models.User import User


def get_all_lists():
    return CateringList.query.all()


def get_all_lists_from_user(user_id):
    return CateringList.query.filter_by(user_id=user_id).all()


def get_list_by_id(id):
    return CateringList.query.get(id)


def create_list(label,
                user_id,
                description,
                max_users,
                session_id,
                item_limit,
                is_active,
                location,
                visibility):
    errors = []
    try:
        db.session.query(User).filter_by(id=user_id).one()
    except NoResultFound:
        errors.append(f"User with id {user_id} does not exist.")

    if errors:  # If there are any errors, return early
        return {"result": None, "errors": errors}

    new_list = CateringList(
        label=label,
        user_id=user_id,
        description=description,
        max_users=max_users,
        session_id=session_id,
        item_limit=item_limit,
        is_active=is_active,
        location=location,
        visibility=visibility
    )
    try:
        db.session.add(new_list)
        db.session.commit()
        db.session.refresh(new_list)
    except IntegrityError:
        db.session.rollback()
        errors.append('There was an error adding the list to the database.')

    return {"result": new_list, "errors": errors}


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
