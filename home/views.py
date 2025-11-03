from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

class FeaturedMenuItemsView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        return MenuItem.objects.filter(is_featured=True)

