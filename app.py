from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
import uuid

# instantiate the app
app = Flask(__name__, static_folder='./dist/static',
            template_folder='./dist')
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': ''}})

# defaultPath = '/api'

Items = [
    {
        'id': uuid.uuid4().hex,
        'name': 'Cake',
        'type': 'Dessert',
        'sweet': True
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Pizza',
        'type': 'Dinner',
        'sweet': False
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Green Eggs and Ham',
        'type': 'Breakfast',
        'sweet': False
    }
]


@app.route('/items', methods=['GET', 'POST'])
def all_items():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        Items.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'type': post_data.get('type'),
            'sweet': post_data.get('sweet')
        })
        response_object['message'] = 'Item added!'
    else:
        response_object['items'] = Items
    return jsonify(response_object)


@app.route('/items/<item_id>', methods=['PUT', 'DELETE'])
def single_item(item_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        edit_item(item_id, post_data)
        response_object['message'] = 'Item updated!'
    if request.method == 'DELETE':
        remove_item(item_id)
        response_object['message'] = 'Item removed!'
    return jsonify(response_object)


def remove_item(item_id):
    for item in Items:
        if item['id'] == item_id:
            Items.remove(item)
            return True
    return False


def edit_item(item_id, updated_item):
    for item in Items:
        if item['id'] == item_id:
            item['name'] = updated_item['payload']['name']
            item['type'] = updated_item['payload']['type']
            item['sweet'] = updated_item['payload']['sweet']
            return True
    return False


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/apple-touch-icon.png', methods=['GET'])
def favicon_apple():
    return send_from_directory(app.template_folder, 'apple-touch-icon.png')


@app.route('/favicon-32x32.png', methods=['GET'])
def favicon_32():
    return send_from_directory(app.template_folder, 'favicon-32x32.png')


@app.route('/favicon-16x16.png', methods=['GET'])
def favicon_16():
    return send_from_directory(app.template_folder, 'favicon-16x16.png')


@app.route('/site.webmanifest', methods=['GET'])
def manifest():
    return send_from_directory(app.template_folder, 'site.webmanifest')


if __name__ == '__main__':
    app.run()
