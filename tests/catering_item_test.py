from datetime import datetime
from main.db.models.Catering import CateringItem
from unittest.mock import Mock
import pytest


class TestCateringItem:

    @pytest.fixture
    def test_repr(self):
        mock_item = Mock(spec=CateringItem)
        mock_item.label = 'Test label'
        mock_item.description = 'Test description'
        mock_item.status = 'pending'
        mock_item.created_at = mock_item.updated_at = datetime.now()
        expected_repr = f"<CateringItem(label={mock_item.label}, description={mock_item.description}, " \
                        f"status={mock_item.status}, created_at={mock_item.created_at}, " \
                        f"updated_at={mock_item.updated_at})>"
        assert expected_repr == mock_item.__repr__()

    def test_id_default(self):
        item = CateringItem()
        assert item.id is None

    def test_label_default(self):
        item = CateringItem()
        assert item.label is None

    def test_type_id_default(self):
        item = CateringItem()
        assert item.type_id is None

    def test_list_id_default(self):
        item = CateringItem()
        assert item.list_id is None

    def test_description_default(self):
        item = CateringItem()
        assert item.description is None

    def test_created_at_default(self):
        item = CateringItem()
        now = datetime.utcnow()
        item.created_at = now
        assert item.created_at == now

    def test_updated_at_default(self):
        item = CateringItem()
        assert item.updated_at is None

    def test_quantity_default(self):
        item = CateringItem()
        item.quantity = 10
        assert item.quantity == 10

    def test_status_default(self):
        item = CateringItem()
        assert item.status is None
