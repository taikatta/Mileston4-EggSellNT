from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Displaying the index page.
    """
    return render(request, "pages/index.html")


def about(request):
    """
    Displaying the about page.
    """
    return render(request, "pages/about.html")