import pytest
from unittest.mock import patch
from main.db.models.User import User
from datetime import datetime
from pytz import utc


class TestUser:
    @pytest.fixture
    def user(self):
        user = User()
        user.id = 1
        user.name = 'Test User'
        user.password = 'hashed_password'
        user.email = 'test@email.com'
        user.last_logged_in = datetime.utcnow()
        user.created_at = datetime.utcnow()
        user.updated_at = datetime.utcnow()
        user.is_active = True
        user.timezone = 'UTC'
        return user

    def test_get_id(self, user):
        assert user.get_id() == '1'

    def test_check_password(self, user):
        with patch('main.db.models.User.check_password_hash', return_value=True):
            assert user.check_password('test_password')

    def test_utc_to_local(self, user):
        local_date = user.utc_to_local(user.created_at)
        assert local_date.tzinfo.zone == user.timezone

    def test_local_last_logged_in(self, user):
        local_date = user.local_last_logged_in
        assert local_date.tzinfo.zone == user.timezone

    def test_local_created_at(self, user):
        local_date = user.local_created_at
        assert local_date.tzinfo.zone == user.timezone

    def test_local_updated_at(self, user):
        local_date = user.local_updated_at
        assert local_date.tzinfo.zone == user.timezone
