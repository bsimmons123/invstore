from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import uuid

# instantiate the app
app = Flask(__name__, static_folder='./dist/static',
            template_folder='./dist')
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': ''}})

defaultPath = '/api'


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


@app.route(f'{defaultPath}/items', methods=['GET', 'POST'])
def all_books():
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


@app.route(f'{defaultPath}/items/<item_id>', methods=['PUT', 'DELETE'])
def single_book(item_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        edit_book(item_id, post_data)
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(item_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


def remove_book(book_id):
    for book in Items:
        if book['id'] == book_id:
            Items.remove(book)
            return True
    return False


def edit_book(book_id, updated_book):
    for book in Items:
        if book['id'] == book_id:
            book['name'] = updated_book['payload']['name']
            book['type'] = updated_book['payload']['type']
            book['sweet'] = updated_book['payload']['sweet']
            return True
    return False


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
