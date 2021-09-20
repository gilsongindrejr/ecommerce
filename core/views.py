from django.views.generic import ListView, TemplateView
from django.shortcuts import render, get_object_or_404, redirect

from products.models import Product, Category


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    paginate_by = 6
    queryset = Product.objects.all()
    context_object_name = 'products'


class CartView(TemplateView):
    template_name = 'cart.html'

    def get(self, request, *args, **kwargs):

        cart = request.session['cart']

        if request.session.get('cart') is None:
            context = {'message': 'Cart is empty'}
        else:
            context = {'cart': {}}
            for product_id in cart:
                context['cart'][product_id] = {
                    'product_obj': Product.objects.filter(id=product_id),
                    'quantity': cart[product_id]['quantity'],
                }

        return render(request, self.template_name, context)


class CartAddView(TemplateView):

    def get(self, request, id, *args, **kwargs):
        if request.session.get('cart') is None:
            request.session['cart'] = {}

        # Product info
        product = get_object_or_404(Product, id=id)
        product_id = str(product.id)
        product_price = str(product.price)
        cart = request.session['cart']

        # Check if product already is on cart
        if product_id not in cart:
            cart[product_id] = {'quantity': 1, 'price': product_price}
        else:
            # if already in cart it only increase the quantity, and limit by 20
            cart[product_id]['quantity'] += 1
            cart[product_id]['quantity'] = min(20, cart[product_id]['quantity'])
            request.session.modified = True
        request.session.modified = True
        return redirect('cart')


class CartRemoveView(TemplateView):
    def get(self, request, id, *args, **kwargs):

        # Product info
        product = get_object_or_404(Product, id=id)
        product_id = str(product.id)
        cart = request.session['cart']

        cart[product_id]['quantity'] -= 1
        if cart[product_id]['quantity'] == 0:
            del cart[product_id]
        request.session.modified = True
        return redirect('cart')


class CartDeleteView(TemplateView):
    def get(self, request, id, *args, **kwargs):

        # Product info
        product = get_object_or_404(Product, id=id)
        product_id = str(product.id)
        cart = request.session['cart']

        del cart[product_id]
        request.session.modified = True
        return redirect('cart')
