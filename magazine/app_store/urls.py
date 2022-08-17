from django.urls import path

from app_store import views

app_name = 'store'


urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('product_test/', views.Product.as_view(), name='product'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category'),
    # path('about_test/', views.About.as_view(), name='about'),
    # path('catalog_test/', views.Catalog.as_view(), name='catalog'),
    # path('index_test/', views.MainTest.as_view(), name='index'),
]
