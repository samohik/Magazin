from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


from account.models import User
from app_store.models import Items


class Order(models.Model):
    CHOICES_DELIVERY = (
        ("delivery", _("Delivery")),
        ("express_delivery", _("Express delivery")),
    )
    CHOICES_PAYMENT = (
        ("card", _("Online card")),
        ("random", _("Online from a random someone else's account")),
    )
    delivery = models.CharField(max_length=100, choices=CHOICES_DELIVERY, default='delivery')
    payment = models.CharField(max_length=100, choices=CHOICES_PAYMENT, default='card')
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True)
    city = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    comments = models.TextField(blank=True)
    error = models.TextField(blank=True)
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'Order {}'.format(self.id)

    # def get_total_cost(self):
    #     return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    user = models.ForeignKey(User, related_name='order_items', on_delete=models.CASCADE)
    order = models.ForeignKey(Order,
                              related_name='order_items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Items,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.user)

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        ordering = ['-id']
