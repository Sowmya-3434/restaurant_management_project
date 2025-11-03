from django.urls import path
from . import FeaturedMenuItemsView

urlpatterns = [
    path('featured-items/',FeaturedMenuItemsView.as_view(), name='featured-items'),
    
]