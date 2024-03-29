
from rest_framework import serializers, viewsets
from .models import *

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [ 'id','name','image', 'parent']