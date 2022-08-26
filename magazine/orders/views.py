from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, TemplateView

from .models import OrderItem, Order
from .forms import OrderCreateForm, PaymentForm
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
            OrderItem.objects.create(
                user=self.request.user,
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
            """Clear cart"""
        cart.clear()
        return HttpResponseRedirect(redirect_to='orders:payment')


class Payment(LoginRequiredMixin, FormView):
    template_name = 'orders/payment.html'
    form_class = PaymentForm

    def get_context_data(self, **kwargs):
        context = super(Payment, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        number = form.cleaned_data['number']
        order = Order.objects.first()
        try:
            if not int(number) % 2 and number[-1] != 0:
                return HttpResponse(f'True {number}, {order}')
            else:
                return HttpResponse(f'False {number}, {order}')
        except BaseException as e:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return HttpResponse(f'False {form}')
