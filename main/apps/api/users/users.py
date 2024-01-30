from flask_login import login_user, login_required, logout_user
from flask_restx import Resource, fields
from flask import request, session, redirect, url_for

from main.apps.api.users import user_api as api
from main.apps.api.users.UserRepository import create_user
from main.db.models.User import User


@api.route('/login', methods=['GET', 'POST'])
class Login(Resource):

    @api.doc('Check if user is logged in')
    def get(self):
        return redirect('/login')

    user_login = api.model('UserCreds', {
        'email': fields.String(required=True, description='Users email'),
        'password': fields.String(required=True, description='Users password')
    })

    @api.doc('Allow user to attempt to login')
    @api.expect(user_login)
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)  # Log in the user
            return {'message': 'Logged in successfully'}
        else:
            return {'message': 'Invalid username or password'}, 401


@api.route('/register', methods=['POST'])
class Register(Resource):
    user_obj = api.model('User', {
        'username': fields.String(required=True, description='Users username'),
        'password': fields.String(required=True, description='Users password'),
        'email': fields.String(required=True, description='Users email')
    })

    @api.doc('Allow creation of new users')
    @api.expect(user_obj)
    def post(self):
        data = api.payload
        username = data['username']
        password = data['password']
        email = data['email']

        # Check if the username or email already exist in the database
        if User.query.filter_by(name=username).first() or User.query.filter_by(email=email).first():
            return {'message': 'Username or email already exists'}, 400

        # Add the new user to the database
        user = create_user(name=username, password=password, email=email)
        login_user(user)

        return {'message': 'User created successfully'}, 201


@api.route('/logout', methods=['GET'])
class Logout(Resource):

    @api.doc('Logout User')
    @login_required
    def get(self):
        # Remove data from session
        logout_user()
        return redirect('/#/login')
