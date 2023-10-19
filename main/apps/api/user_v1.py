from flask import Blueprint
from flask_restx import Api
from werkzeug.exceptions import HTTPException
from .users.users import api as user_api
from ... import defaultPath

user_blueprint = Blueprint('user_api', __name__, url_prefix=defaultPath + '/user/v1')

api = Api(user_blueprint,
          doc='/doc/',
          title='Resource API - User',
          version='1.0',
          description='A description'
          )

api.add_namespace(user_api)


@api.errorhandler(HTTPException)
def handle_error(error: HTTPException):
    """ Handle BluePrint JSON Error Response """
    response = {
        'error': error.__class__.__name__,
        'message': error.description,
    }
    return response, error.code
