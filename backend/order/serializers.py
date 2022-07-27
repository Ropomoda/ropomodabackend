
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *
from account.serializers import AddressSerializer

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Order
        fields = [
                    'status', 
                    'address', 
                    'payment_method', 
                    'is_payed', 
        ]
        
class OrderRowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderRow
        fields = [
                    'order',
                    'product', 
                    'count', 
        ]
        






























