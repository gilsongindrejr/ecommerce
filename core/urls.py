from django.urls import path

from .views import IndexView, CartAddView, CartView, CartRemoveView, CartDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:id>', CartAddView.as_view(), name='add'),
    path('cart/remove/<int:id>', CartRemoveView.as_view(), name='remove'),
    path('cart/delete/<int:id>', CartDeleteView.as_view(), name='delete')
]
