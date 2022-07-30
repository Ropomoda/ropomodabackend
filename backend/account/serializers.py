
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'mobile',
            'email',
        ]
        

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'name', 
            'national_id',
            'phone_number',
        ]

        
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = [
            'uuid',
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
    









































