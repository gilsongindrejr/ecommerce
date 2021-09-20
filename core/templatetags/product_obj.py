from django import template

register = template.Library()


@register.filter
def product_obj(cart, product_id):
    return cart[product_id]['product_obj'][0]


@register.filter
def product_quantity(cart, product_id):
    return cart[product_id]['quantity']


@register.filter
def product_price(cart, product_id):
    return cart[product_id]['product_obj'][0].price


@register.filter
def product_image(cart, product_id):
    return cart[product_id]['product_obj'][0].image.url


@register.filter
def product_total(cart, product_id):
    quantity = int(cart[product_id]['quantity'])
    price = cart[product_id]['product_obj'][0].price
    return quantity * price


@register.filter
def cart_total(cart):
    prices = []
    for product_id, values in cart.items():
        quantity = int(cart[product_id]['quantity'])
        price = cart[product_id]['product_obj'][0].price
        prices.append(quantity * price)
    return sum(prices)

