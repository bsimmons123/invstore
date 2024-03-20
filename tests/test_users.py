import json
from datetime import datetime

import pytest

from main.apps.api.users.UserRepository import get_user_by_email, create_user, UserErrorMsg


def test_logout_redirect_fail(client):
    response = client.get("api/user/v1/user/logout")
    # Check that the redirect couldn't work because the user isn't logged in yet.
    assert response.status == '302 FOUND'
    # Check that the second request was to the index page.


def test_login_fail_email(client):
    data = {"email": "test@gmail", "password": "password", "username": "username"}
    register_resp = client.post("/api/user/v1/user/register", data=json.dumps(data), content_type='application/json')

    # Ensure creation failed
    assert register_resp.status_code == 400
    assert register_resp.json['message'] == UserErrorMsg.INVALID_EMAIL.value


def test_login_fail_name(client):
    data = {"email": "test@gmail", "password": "password", "username": ""}
    register_resp = client.post("/api/user/v1/user/register", data=json.dumps(data), content_type='application/json')

    # Ensure creation failed
    assert register_resp.status_code == 400
    assert register_resp.json['message'] == UserErrorMsg.EMPTY_NAME.value


def test_login_fail_password(client):
    data = {"email": "test@gmail", "password": "passwo", "username": "username"}
    register_resp = client.post("/api/user/v1/user/register", data=json.dumps(data), content_type='application/json')

    # Ensure creation failed
    assert register_resp.status_code == 400
    assert register_resp.json['message'] == UserErrorMsg.SHORT_PASSWORD.value


def test_login_success(client):
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


def test_login_fail(client):
    login_data = {"email": "test@gmail.com", "password": "password"}
    login_response = client.post("/api/user/v1/user/login", data=json.dumps(login_data),
                                 content_type='application/json')

    assert login_response.status_code == 401  # Check the login was successful


def test_user_needed_values(client):
    user = create_user(email="test@gmail.com", password="password", name="test")
    assert user.email == "test@gmail.com"
    assert user.name == "test"
    assert user.timezone == "UTC"
    assert user.id > 0
    assert user.last_logged_in < datetime.utcnow()
    assert user.created_at < datetime.utcnow()
    assert user.updated_at < datetime.utcnow()
    assert user.is_active is True


if __name__ == '__main__':
    pytest.main()
