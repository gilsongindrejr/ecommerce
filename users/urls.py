from django.urls import path

from .views import RegisterView, AddressView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('address', AddressView.as_view(), name='address'),
]
