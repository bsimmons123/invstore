from flask import Flask

from main.extensions.routes_extension import register_routes
from main.extensions.exception_extension import register_exception_handler


def create_app():
    # instantiate the app
    app = Flask(__name__, static_folder='./dist/static',
                template_folder='./dist')

    app.config.from_object(__name__)

    register_routes(app)
    register_exception_handler(app)
    return app
