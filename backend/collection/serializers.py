
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *

class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = [
                    'title_fa', 
                    'title_en', 
                    'slug', 
                    'description', 
                    'image', 
        ]
        






























