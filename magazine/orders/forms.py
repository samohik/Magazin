from django import forms
from django.forms import TextInput

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'delivery', 'payment', 'address', 'postal_code',
            'city', 'comments'
        ]


class PaymentForm(forms.Form):
    number = forms.CharField(
        widget=TextInput(attrs={'type': 'number'}),
        label='Card code', max_length=8, min_length=8, required=True)
