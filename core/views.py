from django.views.generic import ListView, TemplateView

from products.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    paginate_by = 6
    queryset = Product.objects.all()
    context_object_name = 'products'
    
    
class PaymentView(TemplateView):
    pass


class CartView(TemplateView):
    pass

