from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='all'),
    path('products', views.products, name='products'),
    path('farms', views.farms, name='farms'),
    path('<int:product_id>', views.product, name='product'),
    path('search', views.search, name='search'),
]