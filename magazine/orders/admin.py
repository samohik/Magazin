from django.contrib import admin
from .models import Order, OrderItem, Delivery


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity']


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['delivery', 'price', 'discount_limit']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'paid', 'created', 'updated'
    ]
    list_filter = ['paid']
    inlines = [OrderItemInline]
