from django.shortcuts import render


def index(request):
    """
    Displaying the index page.
    """
    return render(request, "pages/index.html")
