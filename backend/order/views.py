from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from account.models import Profile

class OrderList(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class = OrderSerializer
    def get(self, request):
        user = self.request.user
        orders = Order.objects.filter(buyer=user)
        serializer_context={'request': request}
        serializer = OrderSerializer(orders, many=True , context=serializer_context)
        return Response(serializer.data)

