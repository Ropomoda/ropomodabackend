from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductList(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer_context={'request': request}
        serializer = ProductSerializer(products, many=True , context=serializer_context)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer_context={'request': request}
        serializer = ProductSerializer(data=request.data , context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)