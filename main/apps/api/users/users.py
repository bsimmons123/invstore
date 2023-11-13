from flask import session
from flask_restx import Resource

from main.apps.api import check_user_login
from main.apps.api.users import user_api as api


@api.route('/login', methods=['GET'])
class Login(Resource):

    @api.doc('Check if user is logged in')
    def get(self):
        response = check_user_login()
        if response:
            return {'message': 'OH NO! You\'re not logged in :/'}, 401
        else:
            user = session["user"]
            return {'message': 'You\'re logged in!!', 'user': user}, 200
