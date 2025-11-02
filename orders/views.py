from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from .models import Coupon

class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response({'error': 'coupon code is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            coupon = coupon.objects,get(code=code, is_active=True)
        except Coupon.DoesNotExist:
            return Response({'error': 'Invalid or inactive coupon'.}, status=status.HTTP_400_BAD_REQUEST)
        today = date.today(
            if not (coupon.valid_from <= coupon.valid_until):
                return Response({'error': 'coupon is expired or not yet valid.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({
                'success': True,
                'disount_percentage': float(coupon.discount_percentage),
                'message': 'Coupon is valid.'
            }, status=self.HTTP__OK)
        