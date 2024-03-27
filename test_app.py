import unittest
from unittest.mock import patch
from db import ProductModel, create_product, get_product_by_id, update_product, delete_product


class TestProductModel(unittest.TestCase):
    @patch('db.ProductModel.create')
    def test_create_product(self, mock_create):
        # Mocking the ProductModel.create method
        product_data = {"name": "Test Product", "price": 50}
        create_product(**product_data)
        # Verifying that ProductModel.create method was called with the correct arguments
        mock_create.assert_called_once_with(name=product_data["name"], price=product_data["price"])

    @patch('db.ProductModel.get')
    def test_get_product_by_id_found(self, mock_get):
        # Mocking the ProductModel.get method
        product_id = 1
        mock_get.return_value = ProductModel(id=product_id, name="Test Product", price=50)
        product = get_product_by_id(product_id)
        # Verifying that ProductModel.get method was called with the correct argument
        mock_get.assert_called_once_with(ProductModel.id == product_id)
        # Verifying that the returned product is not None
        self.assertIsNotNone(product)
        # Verifying that the returned product has the correct attributes
        self.assertEqual(product.id, product_id)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 50)

    @patch('db.ProductModel.get')
    def test_get_product_by_id_not_found(self, mock_get):
        # Mocking the ProductModel.get method to raise DoesNotExist
        product_id = 1
        mock_get.side_effect = ProductModel.DoesNotExist
        product = get_product_by_id(product_id)
        # Verifying that ProductModel.get method was called with the correct argument
        mock_get.assert_called_once_with(ProductModel.id == product_id)
        # Verifying that the returned product is None
        self.assertIsNone(product)

    @patch('db.ProductModel.get')
    @patch('db.ProductModel.save')
    def test_update_product(self, mock_save, mock_get):
        # Mocking the ProductModel.get and ProductModel.save methods
        product_id = 1
        mock_get.return_value = ProductModel(id=product_id, name="Test Product", price=50)
        update_product(product_id, name="Updated Product", price=100)
        # Verifying that ProductModel.get method was called with the correct argument
        mock_get.assert_called_once_with(ProductModel.id == product_id)
        # Verifying that the product attributes were updated correctly
        self.assertEqual(mock_get.return_value.name, "Updated Product")
        self.assertEqual(mock_get.return_value.price, 100)
        # Verifying that ProductModel.save method was called
        mock_save.assert_called_once()

    @patch('db.ProductModel.get')
    @patch('db.ProductModel.delete_instance')
    def test_delete_product(self, mock_delete_instance, mock_get):
        # Mocking the ProductModel.get and ProductModel.delete_instance methods
        product_id = 1
        mock_get.return_value = ProductModel(id=product_id, name="Test Product", price=50)
        delete_product(product_id)
        # Verifying that ProductModel.get method was called with the correct argument
        mock_get.assert_called_once_with(ProductModel.id == product_id)
        # Verifying that ProductModel.delete_instance method was called
        mock_delete_instance.assert_called_once()


if __name__ == '__main__':
    unittest.main()
