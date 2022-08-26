from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'delivery', 'payment', 'address', 'postal_code',
            'city', 'comments'
        ]


class PaymentForm(forms.Form):
    number = forms.CharField(label='Card code', max_length=8, required=True)
