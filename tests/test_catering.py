import json

import pytest
from flask_login import current_user

from main.apps.api.catering.CateringItemRepository import create_item
from main.apps.api.catering.CateringListRepository import create_list
from main.apps.api.users.UserRepository import get_user_by_email


@pytest.fixture(scope="function")
def login_default_user(client):
    data = {"email": "test@gmail.com", "password": "password", "username": "username"}
    register_resp = client.post("/api/user/v1/user/register", data=json.dumps(data), content_type='application/json')

    # Check if the registration was successful before moving on to the login
    assert register_resp.status_code == 201

    user = get_user_by_email("test@gmail.com")
    assert user.email == "test@gmail.com"

    login_data = {"email": "test@gmail.com", "password": "password"}
    login_response = client.post("/api/user/v1/user/login", data=json.dumps(login_data),
                                 content_type='application/json')

    assert login_response.status_code == 200  # Check the login was successful


def test_catering_itemtypenotexist_fail(client, login_default_user):
    type_id = 1
    test_user = current_user
    list_id = create_list(
        description="test description",
        is_active=True,
        item_limit=6,
        label="test label",
        location="test location",
        max_users=2,
        session_id="123",
        user_id=test_user.id,
        visibility="private"
    )['result'].id
    item = create_item(label="Apple", list_id=list_id, type_id=type_id)

    assert item['errors'][0] == f"CateringItemType with id {type_id} does not exist."


def test_catering_listnotexist_fail(client, login_default_user):
    type_id = 1
    item = create_item(label="Apple", list_id=1, type_id=type_id)

    assert item['errors'][1] == f"CateringList with id {type_id} does not exist."


if __name__ == '__main__':
    pytest.main()
