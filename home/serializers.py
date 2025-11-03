from rest_framework import serializers
from .models import MenuItem
class MenuItemerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'description', 'is_featured']