from store.models.product import Product
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from account.models import Profile

class CartItemCreate(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class = CartSerializer
    def post(self, request):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        cart = Cart.objects.get(profile=profile)
        product = Product.objects.get(id=request.data["product"])
        print(cart)
        cartItem = CartItemSerializer(data=request.data)
        cartItem.cart = cart
        cartItem.product = product

        cartItem.is_valid(raise_exception=True)
        cartItem.save()
        serializer_context={'request': request}
        serializer = CartSerializer(cart , context=serializer_context)
        return Response(serializer.data)

