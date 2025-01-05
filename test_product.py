import pytest
from store import Store
from products import Product


def test_creating_prod():
    """
        Test that creating a normal product works
    """
    product = Product(name="Test product", price=100, quantity=10)

    assert product.name == "Test product"
    assert product.price == 100
    assert product.quantity == 10
    assert product.is_active() is True


def test_creating_prod_invalid_details():
    """
        Test that creating a product with invalid details (empty name, negative price) invokes an exception.
    """
    with pytest.raises(ValueError, match="Invalid input!"):
        Product("", 100, 10)

    with pytest.raises(ValueError, match="Invalid input!"):
        Product("Test product", -100, 10)

    with pytest.raises(ValueError, match="Invalid input"):
        Product("Test product", 100, -10)


def test_prod_becomes_inactive():
    """
        Test that when a product reaches 0 quantity, it becomes inactive.
    """
    prod = Product("Test product", 100, 0)
    with pytest.raises(ValueError):
        prod.is_active()




