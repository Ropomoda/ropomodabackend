
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *
from account.serializers import AddressSerializer
from store.serializers import ProductSerializer
from billing.serializers import PaymentSerializer


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer()
    payment = PaymentSerializer()
    class Meta:
        model = Order
        fields = [
                    'uuid',
                    'status', 
                    'address', 
                    'total_price',
                    'payment', 
        ]
        
class OrderRowSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderRow
        fields = [
                    'uuid',
                    'product', 
                    'quantity', 
        ]
        






























