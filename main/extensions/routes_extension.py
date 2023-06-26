from main.apps.api.profile_v1 import blueprint as profile_api


def register_routes(app):
    """
    Register routes with blueprint and namespace
    """
    app.register_blueprint(profile_api)
