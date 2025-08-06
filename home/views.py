import requests
from django.shortcuts import render

def homepage(requests):
    response = requests.get("http://127.0.0.1:8000/products/menu-api")
    menu = response.json().get('menu',[])
    return render(request, 'home/homepage.html', {'menu': menu})