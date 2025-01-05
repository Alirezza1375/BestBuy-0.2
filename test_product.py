import pytest
from products import Product

def test_create_normal_product():
    product = Product("Test product", 100, 10)
    assert product.name == "Test product"
    assert product.price == 100
    assert product.quantity == 10
    assert product.is_active() is True


def test_create_invalid_input():
    with pytest.raises(ValueError, match="Product name can not be empty!"):
        Product(name="", price=100, quantity=10)
    with pytest.raises(ValueError, match="Price can not be negative!"):
        Product(name="Test product", price=-100, quantity=10)
    with pytest.raises(ValueError, match="Quantity can not be negative!"):
        Product(name="Test product", price=100, quantity=-10)


def test_product_becomes_inactive():
    product = Product("Test product", 100, 1)
    product.buy(1)
    assert product.is_active() is False
    assert product.get_quantity() == 0


def test_product_purchase_updates_quantity():
    product = Product("Test product", 100, 10)
    total_price = product.buy(3)
    assert product.get_quantity() == 7
    assert total_price == 300



def test_buy_larger_quantity():
    product = Product("Test product", 100, 5)
    with pytest.raises(Exception, match="Requested quantity exceeds available stock."):
        product.buy(10)
