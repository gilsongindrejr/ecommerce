import pytest

from products.models import Product, get_file_path

pytestmark = pytest.mark.django_db


@pytest.fixture()
def product():
    return Product(
        name='Test Product',
        price=10.30,
        stock=50,
    )


def test_products_attributes(product):
    assert product.name == 'Test Product'
    assert product.price == 10.30
    assert product.stock == 50


def test_product_str(product):
    assert str(product) == 'Test Product'


def test_product_slug(product):
    product.save()
    assert product.slug == 'test-product'


def test_get_file_path(product):
    file = get_file_path(product, 'file.ext')
    dir = file.split('/')[0]
    filename = file.split('.')[0].split('/')[1]
    ext = file.split('.')[-1]
    assert dir == 'products'
    assert len(filename) == 36
    assert ext == 'ext'
