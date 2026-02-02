from django.shortcuts import render
from .models import About
from .forms import CollaborateRequestForm

# Create your views here.


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateRequestForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "collaborate_form": collaborate_form},
    )