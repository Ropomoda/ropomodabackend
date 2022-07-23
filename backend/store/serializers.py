
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['code', 'name', 'slug', 'price', 'count', 'category', 'description', 'image']
        

        






