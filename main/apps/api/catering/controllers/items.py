import uuid
from flask_restx import Resource
from main.apps.api.catering.controllers import catering_api as api


items = [
    {
        'id': uuid.uuid4().hex,
        'name': 'Cake',
        'type': 'Dessert'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Pizza',
        'type': 'Dinner'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Green Eggs and Ham',
        'type': 'Breakfast'
    }
]

@api.route('/items', methods=['GET', 'POST'])
class ItemList(Resource):

    @api.doc('Get All Catering Items')
    def get(self):
        return items

    @api.doc('Create Catering Item')
    @api.expect(api.parser().add_argument('name', type=str, required=True, help='Name of the item'),
                api.parser().add_argument('type', type=str, required=True, help='Type of the item'))
    def post(self):
        parser = api.parser()
        parser.add_argument('name', type=str, required=True, help='Name of the item')
        parser.add_argument('type', type=str, required=True, help='Type of the item')
        args = parser.parse_args()

        item = {
            'id': uuid.uuid4().hex,
            'name': args['name'],
            'type': args['type'],
        }
        items.append(item)

        return {
            'message': 'Item added!',
            'obj': item
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
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            return True
    return False


def edit_item(item_id, updated_item):
    for item in items:
        if item['id'] == item_id:
            item['name'] = updated_item['name']
            item['type'] = updated_item['type']
            return True
    return False
