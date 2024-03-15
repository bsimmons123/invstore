import json

import pytest


def test_logout_redirect_fail(client):
    response = client.get("api/user/v1/user/logout")
    # Check that the redirect couldn't work because the user isn't logged in yet.
    assert response.status == '302 FOUND'
    # Check that the second request was to the index page.


def test_login_success(client):
    data = {"email": "test@gmail.com", "password": "password", "username": "username"}
    register_resp = client.post("/api/user/v1/user/register", data=json.dumps(data), content_type='application/json')

    # Check if the registration was successful before moving on to the login
    assert register_resp.status_code == 201

    login_data = {"email": "test@gmail.com", "password": "password"}
    login_response = client.post("/api/user/v1/user/login", data=json.dumps(login_data),
                                 content_type='application/json')

    assert login_response.status_code == 200  # Check the login was successful


def test_login_fail(client):
    login_data = {"email": "test@gmail.com", "password": "password"}
    login_response = client.post("/api/user/v1/user/login", data=json.dumps(login_data),
                                 content_type='application/json')

    assert login_response.status_code == 401  # Check the login was successful


if __name__ == '__main__':
    pytest.main()
