from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from app_store.models import Items
from cart.cart import Cart
from cart.forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    """
    Adds an item to the cart.
    :param request:
    :param product_id: int
    :return: redirect
    """
    cart = Cart(request)
    product = get_object_or_404(Items, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    else:
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 update_quantity=cd['update'])

    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    """
    Removes items from the cart.
    :param request:
    :param product_id:
    :return: redirect
    """
    cart = Cart(request)
    product = get_object_or_404(Items, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})





