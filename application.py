import os

from os import environ as env
from flask import Flask, send_from_directory
from flask_login import LoginManager
from dotenv import load_dotenv, find_dotenv
import logging

from main.db.database import init_db
from main.db.models.User import User
from main.extensions.routes_extension import register_routes
from main.extensions.exception_extension import register_exception_handler

logging.basicConfig(level=logging.INFO)

# instantiate the app
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
    print("Environment variables loaded successfully.")
else:
    print("No .env file found.")

app = Flask(__name__, static_folder='./dist', static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = env.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = env.get("SECRET_KEY")

app.logger.info(env.get("SECRET_KEY"))


def create_app():
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user_api.user_login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    init_db(app)

    register_routes(app)
    register_exception_handler(app)

    @app.route('/site.webmanifest')
    def manifest():
        return send_from_directory('dist', 'site.webmanifest')

    # Catch all route
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>', methods=['GET'])
    def catch_all(path):
        return send_from_directory(app.static_folder, 'index.html')

    return app
