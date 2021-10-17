import pytest
from model_bakery import baker
from django.test import Client, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


from users.views import RegisterView, AddressView

pytestmark = pytest.mark.django_db

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def request_obj():
    return RequestFactory()

@pytest.fixture
def user():
    return baker.Baker(get_user_model())


def test_addressview_form_valid_method(client, request_obj, user):
    factory = RequestFactory()
    client = Client()
    form = {
        'zip_code': '11111111',
        'address': 'Street',
        'house_number': '366',
        'complement': 'Complement',
        'neighborhood': 'Neighborhood',
        'city': 'City',
        'state': 'State',
    }
    # post = client.post(path=reverse_lazy('address'), data=form)
    # print(dir(post))

    request = factory.get(reverse_lazy('address'))
    request.user = user

    response = AddressView.as_view()(request)
    print(response)
