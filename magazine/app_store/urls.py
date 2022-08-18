from django.urls import path
from rest_framework import routers
from app_store import views, api

app_name = 'store'

router = routers.DefaultRouter()
# router.register(r'users', api.UserViewSet)
# router.register(r'groups', api.GroupViewSet)

urlpatterns = [
    path('items/', api.ItemsList.as_view()),
    path('', views.Main.as_view(), name='main'),
    path('product_test/', views.Product.as_view(), name='product'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category'),

    # path('about_test/', views.About.as_view(), name='about'),
    # path('catalog_test/', views.Catalog.as_view(), name='catalog'),
    # path('index_test/', views.MainTest.as_view(), name='index'),
]
