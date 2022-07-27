from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.permissions import IsAdminUserOrReadOnly
from .serializers import CollectionSerializer
from .models import *
from .serializers import *

class CollectionViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAdminUserOrReadOnly]
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


    
