from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def view_cart(request):
    """
    Renders the cart contents page
    """
    return render(request, "cart/cart.html")


def add_to_cart(request, id):
    """
    Add a quantity of the specified product to the cart
    """
    try:
        quantity = int(request.POST.get('quantity'))
    except:
        quantity = 1

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('products'))


def adjust_cart(request, id):
    """
    Adjust the quantity of a product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
