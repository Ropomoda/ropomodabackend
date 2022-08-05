
from rest_framework import serializers
from .models import *
from account.serializers import AddressSerializer
from store.serializers import VarietySerializer
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
    variety = VarietySerializer()
    class Meta:
        model = OrderRow
        fields = [
                    'uuid',
                    'variety', 
                    'quantity', 
        ]
        






























