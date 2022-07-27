from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.permissions import IsAdminUserOrReadOnly
from .models import *
from .serializers import *

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAdminUserOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    
