from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products, name='products'),
    path('farms', views.farms, name='farms'),
    path('<int:product_id>', views.product, name='product'),
    path('farm/<int:farm_id>', views.products_by_farm, name='products_by_farm'),
    path('search', views.search, name='search'),
]
