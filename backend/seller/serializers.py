
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *
from account.serializers import UserSerializer
class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = [
                    'uuid',
                    'store_name', 
                    'logo', 
        ]
        






























