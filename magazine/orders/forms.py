from django.utils.translation import gettext_lazy as _

from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    CHOICES_DELIVERY = (
        ("delivery", _("Delivery")),
        ("express_delivery", _("Express delivery")),
    )
    CHOICES_PAYMENT = (
        ("card", _("Online card")),
        ("random", _("Online from a random someone else's account")),
    )

    delivery = forms.ChoiceField(choices=CHOICES_DELIVERY, required=True)
    payment = forms.ChoiceField(choices=CHOICES_PAYMENT, required=True)
    comments = forms.CharField(widget=forms.Textarea,
                               help_text='Optional', required=False)

    class Meta:
        model = Order
        fields = ['address', 'postal_code', 'city']


class Payment(forms.Form):
    pass
