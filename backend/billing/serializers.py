
from rest_framework import serializers
from .models import *
from account.serializers import AddressSerializer

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = [
                    'description',
                    'authority', 
                    'status', 
                    'payment_method', 
                    'ref_id', 
                    'is_payed',
        ]