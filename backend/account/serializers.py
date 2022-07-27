
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'mobile',
        ]
        

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'name', 
        ]
        depth = 1
        
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = [
            'profile',
            'name',
            'description', 
            'longitude', 
            'latitude', 
            'state', 
            'city', 
            'post_address', 
            'plaque', 
            'floor', 
            'post_code', 
        ]
        depth = 2








































