import unittest
from unittest.mock import patch
from db import db, ProductModel, create_product, get_product_by_id, update_product, delete_product


class TestProductModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Connect to the database and create the necessary tables
        db.connect()
        db.create_tables([ProductModel])

    @classmethod
    def tearDownClass(cls):
        # Disconnect from the database
        db.close()

    @patch('db.ProductModel.create')
    def test_create_product(self, mock_create):
        # Mocking the ProductModel.create method
        product_data = {"name": "Test Product", "price": 50}
        create_product(**product_data)
        # Verifying that ProductModel.create method was called with the correct arguments
        mock_create.assert_called_once_with(name=product_data["name"], price=product_data["price"])

    # Add other test methods...


if __name__ == '__main__':
    unittest.main()
