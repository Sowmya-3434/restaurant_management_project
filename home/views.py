from django.conf import settings
from django.shortcuts import render

def home(request):
    context = {
        "phone": settings.Restaurant_Phone
    }
    return render(request, "home/index.html", {
        "restaurant_name": settings.restaurant_name
    })