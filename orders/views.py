from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        Orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)