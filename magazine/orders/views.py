from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


class OrderCreate(LoginRequiredMixin, FormView):
    template_name = 'orders/create.html'
    form_class = OrderCreateForm

    def get_context_data(self, **kwargs):
        context = super(OrderCreate, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['cart'] = Cart(self.request)
        return context

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save()
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
            """Clear cart"""
            cart.clear()
            return render(self.request,
                          'orders/created.html',
                          {'order': order})
