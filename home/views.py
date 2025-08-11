from django.conf import settings
from django.shortcuts import render

def home(request):
    return render(request, "home/index.html", {
        "restaurant_name": settings.restaurant_name
    })