from django.shortcuts import get_object_or_404, render
from .models import Product
from farm.models import Farm
from django.db.models import Q


def index(request):
    return render(request, "products/landing.html")

def farms(request):
    farms = Farm.objects.all()
    return render(request, "products/farms.html", {"farms": farms})

def products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/product.html", {"product": product})
    
def search(request):
    queryset_list = Product.objects.all()

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(description__icontains=keywords) | Q(name__icontains=keywords))

    context = {'products': queryset_list,
        'searchterm': request.GET['keywords']
        }

    return render(request, 'products/search.html', context)
