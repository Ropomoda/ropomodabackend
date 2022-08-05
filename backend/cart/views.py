from django.shortcuts import get_object_or_404
from store.models.variety import Variety
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied , NotAcceptable
from django.utils.translation import ugettext_lazy as _
from order.utils import get_quantity_from_request

class CartItemAPIView(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = CartItem.objects.filter(cart__user=user)
        return queryset


    def get(self, request , *args , **kwargs):
        user = self.request.user
        cart = get_object_or_404(Cart,user=user)

        cartItems = CartItem.objects.filter(
            cart=cart,
        )
        serializer_context={'request': request}
        serializer = CartItemSerializer(cartItems , many=True , context=serializer_context)
        return Response(serializer.data)
    def post(self, request , *args , **kwargs):
        user = self.request.user
        cart = get_object_or_404(Cart,user=user)
        try:
            variety = get_object_or_404(Variety,uuid=request.data["variety"])
        except Exception as e:
            raise NotAcceptable("Please Enter a variety")
        current_item = CartItem.objects.filter(cart=cart , variety=variety)

        if variety.seller == user:
            raise PermissionDenied("This is Your Product")
        if len(current_item) > 0:
            raise NotAcceptable("You Already have this item in your cart")
        
        quantity = get_quantity_from_request(request , variety)
        cartItem = CartItem(cart=cart, variety = variety, quantity = quantity)
        cartItem.save()
        serializer_context={'request': request}
        serializer = CartItemSerializer(cartItem , context=serializer_context)
        return Response(serializer.data)



class CartItemView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = CartSerializer
    queryset = CartItem.objects.all()
    lookup_field = "uuid"

    def get(self, request , *args , **kwargs):
        user = self.request.user
        cart_item = self.get_object()
        if cart_item.cart.user != user:
            raise PermissionDenied("This cart does not belong to you")
        serializer_context={'request': request}
        serializer = CartItemSerializer(cart_item , many=True , context=serializer_context)
        return Response(serializer.data)

    def patch(self, request , *args , **kwargs):
        user = self.request.user
        cart_item = self.get_object()
        
        product = cart_item.product

        try:
            quantity = int(request.data["quantity"])
        except Exception as e:
            raise NotAcceptable("Please Enter your quantity")

        if cart_item.cart.user != user:
            raise PermissionDenied("This cart does not belong to you")
        if quantity > product.inventory:
            raise NotAcceptable("Your Entered quantity is more then inventory")
        if quantity > product.max_quantity:
            raise NotAcceptable("Your Entered quantity is more then max allowed quantity")

        cart_item.quantity = quantity
        cart_item.save()
        serializer_context={'request': request}
        serializer = CartItemSerializer(cart_item , context=serializer_context)
        return Response(serializer.data)

    def delete(self,request , *args , **kwargs):
        user = self.request.user
        cart_item = self.get_object()
        if cart_item.cart.user != user:
            raise PermissionDenied("This cart does not belong to you")
        
        cart_item.delete()

        return Response({
            "detail": _("your item is deleted")
        } , status=status.HTTP_204_NO_CONTENT)