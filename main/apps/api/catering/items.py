from flask import request
from flask_login import login_required, current_user
from flask_restx import Resource, fields

from main.apps.api.catering import catering_api as api
from main.apps.api.catering.CateringItemRepository import create_item
from main.apps.api.catering.CateringItemTypeRepository import get_item_by_user_id
from main.apps.api.catering.CateringListRepository import get_list_by_id


def serialize_type(item_type):
    return {
        'id': item_type.id,
        'label': item_type.label
    }


@api.route('/items', methods=['GET', 'POST'])
class ItemList(Resource):

    @api.doc('Get All Catering Items')
    @api.expect(api.parser().add_argument('listId', type=int, required=True, help='Name of the item'))
    @login_required
    def get(self):
        user_id = current_user.id
        list_id = request.args.get("listId")
        # Assuming CateringItem is the model for your items
        catering_list = get_list_by_id(id=list_id)
        items = catering_list.catering_items
        types = get_item_by_user_id(user_id=user_id)

        # Convert items to a format suitable for response
        items_response = [{'id': item.id, 'label': item.label, 'type': serialize_type(item.type), 'list_id': list_id} for item in items]
        types_response = [{'id': itemType.id, 'label': itemType.label} for itemType in types]

        return {'items': items_response, 'types': types_response}

    item_obj = api.model('Item', {
        'name': fields.String(required=True, description='Item Name'),
        'type_id': fields.String(required=True, description='Item Type Id'),
        'list_id': fields.String(required=True, description='Item Type Id'),
    })

    @api.doc('Create Catering Item')
    @api.expect(item_obj)
    def post(self):
        data = api.payload
        name = data['label']
        type_id = data['type_id']
        list_id = data['list_id']

        new_item = create_item(label=name, type_id=type_id, list_id=list_id)

        return {
            'message': 'Item added!',
            'obj': {
                'id': new_item.id,
                'label': new_item.label,
                'type': serialize_type(new_item.type),
                'list_id': list_id
            }
        }


@api.route('/items/<item_id>', methods=['PUT', 'DELETE'])
class MutateItem(Resource):
    @api.doc('Update Catering Item')
    @api.expect(api.parser().add_argument('name', type=str, required=True, help='Name of the item'),
                api.parser().add_argument('type', type=str, required=True, help='Type of the item'),
                api.parser().add_argument('id', type=str, required=True, help='Name of the item'))
    def put(self, item_id: str):
        parser = api.parser()
        parser.add_argument('name', type=str, required=True, help='Name of the item')
        parser.add_argument('type', type=str, required=True, help='Type of the item')
        parser.add_argument('id', type=str, required=True, help='ID of the item')
        args = parser.parse_args()
        edit_item(item_id, args)
        return {'message': 'Item updated!'}

    @api.doc('Delete Catering Item')
    def delete(self, item_id: str):
        item_removed = remove_item(item_id)
        if item_removed:
            return {'message': 'Item removed!'}
        return {'message': 'Item NOT removed!'}


def remove_item(item_id):
    # for item in items:
    #     if item['id'] == item_id:
    #         items.remove(item)
    #         return True
    return False


def edit_item(item_id, updated_item):
    # for item in items:
    #     if item['id'] == item_id:
    #         item['name'] = updated_item['name']
    #         item['type'] = updated_item['type']
    #         return True
    return False
