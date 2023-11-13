import os
import unittest
from flask import Flask
from flask_login import LoginManager

from main.apps.api.catering.CateringItemRepository import create_item
from main.apps.api.catering.CateringItemTypeRepository import create_item_type
from main.apps.api.catering.CateringListRepository import create_list
from main.db.database import init_db, db
from main.extensions.exception_extension import register_exception_handler
from main.extensions.routes_extension import register_routes


class TestItems(unittest.TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        init_db(app)

        register_routes(app)
        register_exception_handler(app)

        return app

    def setUp(self):
        self.app = self.create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client.post('/api/user/v1/user/register',
                                json={'username': 'test', 'password': 'password', 'email': 'test@example.com'})
        self.user = User.query.filter_by(email='test@example.com').first()

    def tearDown(self):
        # Remove the application context and drop all tables
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_items_empty(self):
        response = self.client.get('/api/catering/v1/catering/items?listId=1')
        self.assertEqual(response.status_code, 404)
        # Add more assertions to validate the response content if needed

    def test_get_items(self):
        create_list(label='list', user_id=self.user.id)
        create_item_type(label='type', user_id=self.user.id)
        create_item(label='item', type_id='1', list_id='1')
        response = self.client.get('/api/catering/v1/catering/items?listId=1')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response content if needed


    def test_post_item(self):
        create_item_type(label='label', user_id=self.user.id)
        payload = {
            'label': 'Test Item',
            'type_id': '1',
            'list_id': '1'
        }
        response = self.client.post('/api/catering/v1/catering/items', json=payload)
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response content if needed

    def test_put_item(self):
        args = {'name': 'Updated Name', 'type': 'Updated Type', 'id': '1'}
        response = self.client.put('/api/catering/v1/catering/items/1', query_string=args)
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response content if needed

    def test_delete_item(self):
        response = self.client.delete('/api/catering/v1/catering/items/1')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response content if needed

    def test_get_item_types_empty(self):
        response = self.client.get('/api/catering/v1/catering/item_types?listId=1')
        self.assertEqual(response.status_code, 404)
        # Add more assertions to validate the response content if needed

    def test_get_item_types(self):
        create_list(label='list', user_id=self.user.id)
        create_item_type(label='type', user_id=self.user.id)
        create_item(label='item', type_id='1', list_id='1')
        response = self.client.get('/api/catering/v1/catering/item_types?listId=1')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response content if needed

    def test_post_item_type(self):
        payload = {'label': 'Test Item Type'}
        response = self.client.post('/api/catering/v1/catering/item_types', json=payload)
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response content if needed


if __name__ == '__main__':
    unittest.main()
