from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CollectionSerializer
from .models import *
from .serializers import *

class CollectionViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


    
