from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import Order, OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
from django.contrib.auth.models import User
import stripe

stripe.api_key = settings.STRIPE_SECRET


def user_order(request):
    """
    Displays user's order history, by date of purchase.
    """
    orders = request.user.orders.all()
    order_items = []
    for order in orders:
        order_products = OrderLineItem.objects.filter(order=order)
        total = 0
        for prod in order_products:
             total += prod.quantity * prod.product.price
        order_items.append({"order": order, "items": order_products, "total": total})
    return render(request, "pages/profile.html", {"orders": order_items})


@login_required(login_url='login')
def checkout(request):
    """
    Renders checkout page -
    by clicking "Submit Payment" button the payment is processed
    """
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = request.user
            order.save()
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request,
                                 "You have successfully paid! Thank you!")
                request.session['cart'] = {}
                return redirect(reverse('user_order'))
            else:
                messages.error(request,
                               "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request,
                           "Unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request,
                  "checkout/checkout.html",
                  {'order_form': order_form,
                   'payment_form': payment_form,
                   'publishable': settings.STRIPE_PUBLISHABLE})
