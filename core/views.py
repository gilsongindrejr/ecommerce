from django.views.generic import ListView

from products.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    paginate_by = 6
    ordering = Product.name
    queryset = Product.objects.all()
    context_object_name = 'products'

