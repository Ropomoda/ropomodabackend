
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *
from seller.serializers import SellerSerializer
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    seller = SellerSerializer()
    class Meta:
        model = Product
        fields = [
                    'id',
                    'code',
                    'title_fa', 
                    'title_en', 
                    'slug', 
                    'rrp_price', 
                    'selling_price', 
                    'inventory', 
                    'max_quantity', 
                    'category', 
                    'active_collection',
                    'is_promotion',
                    'description',
                    'image',
                    'seller',
        ]
        






























