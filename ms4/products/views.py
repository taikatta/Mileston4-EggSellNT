from django.shortcuts import get_object_or_404, render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/product.html", {"product": product})