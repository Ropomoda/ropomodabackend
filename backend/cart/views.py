from django.shortcuts import get_object_or_404
from store.models.product import Product
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied , NotAcceptable

class CartItemAPIView(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class = CartSerializer
    def post(self, request):
        user = self.request.user
        cart = get_object_or_404(Cart,user=user)
        product = get_object_or_404(Product,pk=request.data["product"])
        current_item = CartItem.objects.filter(cart=cart , product=product)

        if product.seller == user:
            return PermissionDenied("This is Your Product")
        if len(current_item) > 0:
            return NotAcceptable("You Already have this item in your cart")
        
        try:
            quantity = int(request.data["quantity"])
        except Exception as e:
            return NotAcceptable("Please Enter your quantity")

        if quantity > product.inventory:
            return NotAcceptable("Your Entered quantity is more then inventory")
        if quantity > product.max_quantity:
            return NotAcceptable("Your Entered quantity is more then max allowed quantity")
        cartItem = CartItemSerializer(data=request.data)
        cartItem.cart = cart
        cartItem.product = product

        cartItem.is_valid(raise_exception=True)
        cartItem.save()
        serializer_context={'request': request}
        serializer = CartSerializer(cart , context=serializer_context)
        return Response(serializer.data)

