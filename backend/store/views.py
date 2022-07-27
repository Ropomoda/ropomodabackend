from django.shortcuts import get_object_or_404
from app.permissions import IsAdminUserOrReadOnly
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductList(APIView):
    permission_classes=[IsAdminUserOrReadOnly]
    serializer_class = ProductSerializer
    def get(self, request):
        category_id = self.request.query_params.get('category')
        collection_id = self.request.query_params.get('category')
        if(category_id):
            products = Product.objects.filter(category=category_id)
        elif (collection_id):
            products = Product.objects.filter(active_collection=collection_id)
        else:
            products = []
        serializer_context={'request': request}
        serializer = ProductSerializer(products, many=True , context=serializer_context)
        return Response(serializer.data)

class ProductDetail(APIView):
    permission_classes=[IsAdminUserOrReadOnly]
    serializer_class = ProductSerializer
    def get(self, request,code=None):
        product = get_object_or_404(Product , code=code)
        serializer_context={'request': request}
        serializer = ProductSerializer(product, context=serializer_context)
        return Response(serializer.data)