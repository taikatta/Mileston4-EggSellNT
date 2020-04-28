from django.shortcuts import get_object_or_404, render
from .models import Product
from farm.models import Farm
from django.db.models import Q


def farms(request):
    """
    Renders farms page - farms where the eggs are from
    """
    farms = Farm.objects.all()
    return render(request, "products/farms.html", {"farms": farms})


def products(request):
    """
    Renders products page - showing all our products
    """
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})


def products_by_farm(request, farm_id):
    """
    Renders products page - showing products from the selected farm
    """
    farm = get_object_or_404(Farm, pk=farm_id)
    products = farm.products.all()
    return render(request, "products/products.html", {"products": products})


def product(request, product_id):
    """
    Renders product page - showing more details about that product
    """
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/product.html", {"product": product})


def search(request):
    """
    The user can search in product's name and in their description
    """
    queryset_list = Product.objects.all()

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                Q(description__icontains=keywords) | Q(name__icontains=keywords))

    context = {'products': queryset_list,
               'searchterm': request.GET['keywords']
               }

    return render(request, 'products/products.html', context)
