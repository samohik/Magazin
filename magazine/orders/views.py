from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView

from .tasks import validator, adding_task

from cart.cart import Cart
from .forms import OrderCreateForm, PaymentForm
from .models import OrderItem, Order


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
        context['form'] = PaymentForm(self.request.GET)
        context['order'] = Order.objects.filter(user=self.request.user).first().payment
        return context

    def post(self, request, *args, **kwargs):
        order = Order.objects.filter(user=self.request.user).first()
        answer = self.get_context_data()['order']
        if answer == 'random':
            number = request.POST['Code']
            validator.delay(number)
            return HttpResponse('«Ждём подтверждения оплаты платёжной системы')
        else:
            form = PaymentForm(request.POST)
            if form.is_valid():
                number = form.cleaned_data['number']
                validator.delay(number)
                return HttpResponse('«Ждём подтверждения оплаты платёжной системы')
            else:
                context = {
                    'form': PaymentForm(request.GET),
                    'order': Order.objects.filter(user=self.request.user).first().payment
                }
                return render(request, self.template_name, context)

