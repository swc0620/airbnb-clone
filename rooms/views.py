from django.shortcuts import render
from . import models

# Create your views here.

def all_rooms(request):
    # render function works on top of the HTTPResponse function.
    # render function not only gives the http response but also compiles html file into python file and renders it
    all_rooms = models.Room.objects.all()[:5]
    return render(request, "rooms/home.html", context={"rooms": all_rooms})

    # context is how you send variable from view to template