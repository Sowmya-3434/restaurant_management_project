from rest_framework import serializers
from .models import order

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = ['order_id', 'date', 'total_prices', 'customer']