from django.shortcuts import render
from team.models import Team

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
    team = Team.objects.all()
    return render(request, "pages/about.html", {"team": team})


