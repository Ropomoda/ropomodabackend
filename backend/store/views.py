from django.shortcuts import render
from rest_framework import routers, serializers, viewsets

from .models import *
from .serializers import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    
