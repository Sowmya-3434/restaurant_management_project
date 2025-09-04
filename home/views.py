from django.shortcuts import render
from .models import restaurant_name

def home(request):
    restaurant = Restauarnt.objects.first(
        return render(request, 'HTML_home.html', {'restaurant': restaurant})
    )