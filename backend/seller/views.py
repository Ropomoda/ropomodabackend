from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *

class SellerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


    
