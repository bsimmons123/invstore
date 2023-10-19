import os

from flask import Flask, render_template
from flask_login import LoginManager

from main.db.database import init_db
from main.db.models.User import User
from main.extensions.routes_extension import register_routes
from main.extensions.exception_extension import register_exception_handler


def create_app():
    # instantiate the app
    app = Flask(__name__, static_folder='./dist/static',
                template_folder='./dist')

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    login_manager = LoginManager(app)
    login_manager.login_view = 'user_api.user_login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    init_db(app)

    register_routes(app)
    register_exception_handler(app)

    # This route will serve your Vue app for any routes that aren't API routes.
    @app.route('/<path:path>', methods=['GET'])
    def catch_all(path):
        return render_template('index.html')

    return app
