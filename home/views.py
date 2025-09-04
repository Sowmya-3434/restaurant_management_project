from django.shortcuts import render
from .models import restaurant_name

def menu(request):
    items = MenuItem.objects.all(
    return render(request, 'HTML_menu.html', {'items': items})
    )