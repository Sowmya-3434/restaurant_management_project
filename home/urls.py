from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.contact_view, name='menu'),
    
]