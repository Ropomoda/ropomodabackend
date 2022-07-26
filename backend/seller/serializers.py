
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *

class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = [
                    'profile', 
                    'store_name', 
                    'logo', 
        ]
        






























