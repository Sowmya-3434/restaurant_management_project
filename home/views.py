from django.conf import settings
from django.shortcuts import render

def home(request):
    context = {
        "phone": settings.RESTAURANT_PHONE
    }
    return render(request, "home.html", context)