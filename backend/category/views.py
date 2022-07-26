from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    
