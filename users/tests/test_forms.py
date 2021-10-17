import pytest

from users.forms import AddressForm

pytestmark = pytest.mark.django_db


@pytest.fixture()
def address_form():
    form = AddressForm()
    form.zip_code = '11111111'
    form.address = 'Street'
    form.house_number = '366'
    form.complement = 'Complement'
    form.neighborhood = 'Neighborhood'
    form.city = 'City'
    form.state = 'State'
    return form


def test_address_form(address_form):
    assert address_form.zip_code == '11111111'
    assert address_form.address == 'Street'
    assert address_form.house_number == '366'
    assert address_form.complement == 'Complement'
    assert address_form.neighborhood == 'Neighborhood'
    assert address_form.city == 'City'
    assert address_form.state == 'State'
