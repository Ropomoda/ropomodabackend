
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *
from account.serializers import AddressSerializer
from store.serializers import ProductSerializer

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Order
        fields = [
                    'id',
                    'status', 
                    'address', 
                    'payment_method', 
                    'is_payed', 
        ]
        
class OrderRowSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderRow
        fields = [
                    'id',
                    'order',
                    'product', 
                    'quantity', 
        ]
        






























