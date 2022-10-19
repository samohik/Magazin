from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from account.models import User
from app_store.models import Items


class Delivery(models.Model):
    delivery = models.CharField(verbose_name='Delivery', max_length=50)
    price = models.PositiveIntegerField(verbose_name='Price')
    discount_limit = models.PositiveIntegerField(verbose_name='Discount',
                                                 default=2000, blank=True)

    def __str__(self):
        return str(self.delivery)


class Order(models.Model):
    CHOICES_PAYMENT = (
        ("card", _("Online card")),
        ("random", _("Online from a random someone else's account")),
    )
    delivery = models.ForeignKey('Delivery', related_name='order', on_delete=models.CASCADE, blank=True, null=True)
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

    def get_absolute_url(self):
        return reverse('account:order_history_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'Order {}'.format(self.id)

    # noinspection PyTypeChecker
    def get_total_cost(self):
        delivery = self.delivery
        total = sum(item.get_cost() for item in self.order_items.all())
        if delivery:
            if delivery.discount_limit:
                if total < delivery.discount_limit:
                    return self.get_cost_with_delivery(delivery, total)
                else:
                    return total
            else:
                return self.get_cost_with_delivery(delivery, total)
        else:
            return total

    def get_cost_with_delivery(self, delivery, total):
        dis_total = total + delivery.price
        return dis_total


class OrderItem(models.Model):
    user = models.ForeignKey(User, related_name='order_items', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='order_items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Items, related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.user)

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        ordering = ['-id']
