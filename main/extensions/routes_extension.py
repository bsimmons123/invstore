from main.apps.api.catering_v1 import catering_blueprint as catering_api
from main.apps.api.user_v1 import user_blueprint as user_api


def register_routes(app):
    """
    Register routes with blueprint and namespace
    """
    app.register_blueprint(catering_api)
    app.register_blueprint(user_api)
