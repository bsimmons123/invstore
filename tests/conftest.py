import pytest
from flask import Flask
from flask_login import LoginManager

from application import create_app
from main.db.database import init_db
from main.db.models.User import User
from main.extensions.exception_extension import register_exception_handler
from main.extensions.routes_extension import register_routes


@pytest.fixture()
def app():
    app = Flask(__name__)
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": 'sqlite:///:memory:',
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "DEBUG": False
    })

    app.secret_key = "secret key"

    init_db(app)
    # other setup can go here

    register_routes(app)
    register_exception_handler(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user_api.user_login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()



@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
