from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.OrderCreate.as_view(), name='order_create'),
    path('payment/<int:order_id>/', views.Payment.as_view(), name='payment'),
]
