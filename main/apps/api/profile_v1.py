from flask import Blueprint
from flask_restx import Api
from werkzeug.exceptions import HTTPException
from .catering.controllers.items import api as catering_api
from ... import defaultPath

blueprint = Blueprint('catering_api', __name__, url_prefix=defaultPath + '/catering/v1')

api = Api(blueprint,
          doc='/doc/',
          title='Resource API - Profile',
          version='1.0',
          description='A description'
          )

api.add_namespace(catering_api)


@api.errorhandler(HTTPException)
def handle_error(error: HTTPException):
    """ Handle BluePrint JSON Error Response """
    response = {
        'error': error.__class__.__name__,
        'message': error.description,
    }
    return response, error.code
