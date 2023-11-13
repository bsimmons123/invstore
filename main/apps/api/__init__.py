from datetime import datetime

from flask import session, redirect


def check_user_login():
    if "user" not in session or not is_token_valid(session["user"]):
        # Redirect to login or perform other actions for an expired session
        return redirect("/login")
    # If the session is valid, you can add any additional logic here if needed


def is_token_valid(token):
    # Check if the token has an expiration time
    if "expires_at" in token:
        expires_at = datetime.fromtimestamp(token["expires_at"])
        return expires_at > datetime.now()
    return False
