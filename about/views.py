from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateRequestForm

# Create your views here.


def about_me(request):
    """
    Renders the most recent information on the website owner's about me page
    and handles collaboration requests submitted via the form.
    Displays an instance of :model:`about.About`.
    **Context**

    ``about``
        An instance of :model:`about.About`.

    ``collaborate_form``
        An instance of :class:`~about.forms.CollaborateRequestForm`.
    **Template:**
    :template:`about/about.html`
    """
    if request.method == "POST":
        collaborate_form = CollaborateRequestForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for your request. We will get back to you soon.")

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateRequestForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "collaborate_form": collaborate_form},
    )
