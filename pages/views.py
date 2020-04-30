from django.shortcuts import render
from company.models import Employee


def index(request):
    """
    Displaying the index page.
    """
    return render(request, "pages/index.html")


def about(request):
    """
    Displaying the about us page.
    """
    employees = Employee.objects.all()
    return render(request, "pages/about.html", {"employees": employees})
