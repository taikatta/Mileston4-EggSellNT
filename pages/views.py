from django.shortcuts import render
from company.models import Employee


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
    company = Employee.objects.all()
    return render(request, "pages/about.html", {"company": company})
