from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem


def register(request):
    """
    Users can register a new account, after registering user
    is redirected to the home page.
    """
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':

        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if the two passwords match
        if password == password2:

            # Check if username exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already registered.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,
                                   'That email is already used! Please choose a different one.')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,
                                                    password=password,
                                                    email=email,
                                                    first_name=first_name,
                                                    last_name=last_name)

                    # Login after register
                    auth.login(request, user)
                    messages.success(request, 'Welcome!')
                    return redirect('index')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    """
    Renders the login page
    """
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Using authenticate() to verify a set of credentials:
        user = auth.authenticate(username=username, password=password)

        # Check if the credentials are valid for a backend:
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome!')
            return redirect('index')
        else:
            messages.error(request,
                           "Invalid credentials, please try it again!")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    """
    Logout the user
    """
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out!")
    return redirect('index')
