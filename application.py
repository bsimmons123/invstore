from datetime import datetime, timedelta
from os import environ as env
from urllib.parse import urlencode, quote_plus

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv

from flask import Flask, render_template, send_from_directory, url_for, redirect, session

from main.apps.api import check_user_login
from main.apps.api.users.UserRepository import create_user
from main.db.database import init_db
from main.db.models.User import User
from main.extensions.routes_extension import register_routes
from main.extensions.exception_extension import register_exception_handler

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
    print("Environment variables loaded successfully.")
else:
    print("No .env file found.")

app = Flask(__name__, static_folder='./dist', static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = env.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = env.get("APP_SECRET_KEY")

oauth = OAuth(app)


def create_app():
    # instantiate the app
    oauth.register(
        "auth0",
        client_id=env.get("AUTH0_CLIENT_ID"),
        client_secret=env.get("AUTH0_CLIENT_SECRET"),
        client_kwargs={
            "scope": "openid profile email",
        },
        server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
    )

    init_db(app)

    register_routes(app)
    register_exception_handler(app)

    @app.route('/site.webmanifest')
    def manifest():
        return send_from_directory('dist', 'site.webmanifest')

    @app.route("/login")
    def login():
        response = check_user_login()
        if not response:
            return redirect("/")
        return oauth.auth0.authorize_redirect(
            redirect_uri=url_for("callback", _external=True)
        )

    @app.route("/callback", methods=["GET", "POST"])
    def callback():
        try:
            token = oauth.auth0.authorize_access_token()
            # Check if the token has an expiration time
            if "expires_in" in token:
                expires_at = datetime.now() + timedelta(seconds=token["expires_in"])
                token["expires_at"] = expires_at.timestamp()

            user_id = token["userinfo"]["sub"]
            if User.query.filter_by(id=user_id).first():
                session["user"] = token
                return redirect("/")

            name = token["userinfo"]["nickname"]
            email = token["userinfo"]["email"]

            create_user(id=user_id, name=name, email=email)

            # Store the token in the session
            session["user"] = token
            return redirect("/")
        finally:
            return redirect("/")

    @app.route("/logout")
    def logout():
        response = check_user_login()
        if response:
            return redirect("/")
        session.clear()
        return redirect(
            "https://" + env.get("AUTH0_DOMAIN")
            + "/v2/logout?"
            + urlencode(
                {
                    "returnTo": url_for("catch_all", path='', _external=True),
                    "client_id": env.get("AUTH0_CLIENT_ID"),
                },
                quote_via=quote_plus,
            )
        )

    # Catch all route
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>', methods=['GET'])
    def catch_all(path):
        return send_from_directory(app.static_folder, 'index.html')

    return app
