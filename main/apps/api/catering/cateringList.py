from flask import session, request, jsonify
from flask_login import login_required, current_user
from flask_restx import Resource, fields

from main.apps.api.catering import catering_api as api
from main.apps.api.catering.CateringListRepository import get_all_lists_from_user, create_list


@api.route('/catering_list', methods=['GET', 'POST'])
class CateringList(Resource):

    @api.doc('Get All Catering Lists')
    @login_required
    def get(self):
        user_id = current_user.id
        # Assuming CateringItem is the model for your items
        lists = get_all_lists_from_user(user_id)

        # Convert items to a format suitable for response
        response = jsonify([{
            'id': lst.id,
            'label': lst.label,
            'user_id': lst.user_id,
        } for lst in lists])

        return response

    create_list = api.model('CateringList', {
        'label': fields.String(required=True, description='List label/name')
    })

    @api.doc('Create Catering List')
    @api.expect(create_list)
    @login_required
    def post(self):
        data = api.payload
        label = data['label']
        user_id = current_user.id

        catering_list = create_list(user_id=user_id, label=label)

        return {'message': 'Item added!'}, 200

