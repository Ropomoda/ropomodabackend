
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
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = [
            'user',
            'name', 
        ]

        
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
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
    









































