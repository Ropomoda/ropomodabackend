
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from .models import *
from account.serializers import UserSerializer
from store.serializers import VarietySerializer

class CartSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Cart
        fields = [
            'user',
        ]
        
class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    variety = VarietySerializer()

    class Meta:
        model = CartItem
        fields = [
            'uuid',
            'variety',
            'quantity',
        ]
        




