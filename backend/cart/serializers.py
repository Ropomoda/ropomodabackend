
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from .models import *
from account.serializers import UserSerializer
from store.serializers import ProductSerializer

class CartSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Cart
        fields = [
            'user',
        ]
        
class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    cart = CartSerializer()
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = [
            'cart',
            'product',
            'count',
        ]
        




