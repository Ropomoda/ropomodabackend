from django.shortcuts import get_object_or_404
from account.models.address import Address
from store.models.product import Product
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.generics import ListCreateAPIView , RetrieveDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied , NotAcceptable
from django.utils.translation import ugettext_lazy as _
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from account.models import Profile
from .utils import get_quantity_from_request

class OrderAPIView(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(buyer=user)
        return queryset

    def get(self, request , *args , **kwargs):
        orders = self.get_queryset()
        serializer_context={'request': request}
        serializer = OrderSerializer(orders, many=True , context=serializer_context)
        return Response(serializer.data)

    def post(self, request , *args , **kwargs):
        user = self.request.user
        orders = self.get_queryset().filter(is_closed=False)
        
        if len(orders) > 10:
            raise NotAcceptable("Your number of Orders has exceeded limit")

        try:
            address_id = request.data["address"]
            address = get_object_or_404(Address,pk=address_id)
        except Exception as e:
            raise NotAcceptable("Please Enter an Address")

        try:
            payment_method = request.data["payment_method"]
        except Exception as e:
            raise NotAcceptable("Please Enter a payment_method")

        order = Order.objects.create(
            buyer=user,
            address=address,
            payment_method=payment_method,
        )

        serializer_context={'request': request}
        serializer = OrderSerializer(order , context=serializer_context)
        return Response(serializer.data , status=status.HTTP_201_CREATED)

class OrderView(RetrieveDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    def get(self, request , *args , **kwargs):
        user = self.request.user
        order = self.get_object()

        if order.buyer != user:
            raise PermissionDenied("This Order does not belong to you")

        serializer_context={'request': request}
        serializer = OrderSerializer(order , context=serializer_context) 
        return Response(serializer.data)

    def delete(self, request , *args , **kwargs):
        user = self.request.user
        order = self.get_object()

        if order.buyer != user:
            raise PermissionDenied("This Order does not belong to you")
        if order.status > 3:
            raise NotAcceptable("This Order can not cancelable")
        order.status = 12
        order.is_closed = True

        orderRows = OrderRow.objects.filter(order=order)
        for orderRow in orderRows:
            product = orderRow.product
            product.inventory += orderRow.quantity
            product.save()

        return Response({
            "detail": _("Order Canceled")
        } , status=status.HTTP_204_NO_CONTENT)

class OrderRowAPIView(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_order_rows(self):
        user = self.request.user
        order = self.get_object()
        if order.buyer != user:
            raise PermissionDenied("This order does not belong to you")
        queryset = OrderRow.objects.filter(order=order)
        return queryset

    def get(self, request , *args , **kwargs):
        orderRows = self.get_order_rows()
        serializer_context={'request': request}
        serializer = OrderRowSerializer(orderRows, many=True , context=serializer_context)
        return Response(serializer.data)

    def post(self, request , *args , **kwargs):
        user = self.request.user
        orderRows = self.get_order_rows()
        order = self.get_object()
        current_item = OrderRow.objects.filter(order=order , product=product)

        if len(orderRows) > 20:
            raise NotAcceptable("If you want ordering more then 10 products, please send a ticket to us!")

        try:
            product = get_object_or_404(Product,pk=request.data["product"])
        except Exception as e:
            raise NotAcceptable("Please Enter a Product")

        if order.status != 0:
            raise NotAcceptable("You cannot add item to in process order")
        if product.seller == user:
            raise PermissionDenied("This is Your Product")

        if product.seller == user:
            raise PermissionDenied("This is Your Product")
        if len(current_item) > 0:
            raise NotAcceptable("You already have this item in your order")
        
        orderRow = OrderRow(order=order, product = product, quantity = quantity)
        orderRow.save()

        quantity = get_quantity_from_request(request , product)
        product.inventory -= quantity
        product.save()

        serializer_context={'request': request}
        serializer = OrderRowSerializer(orderRow , context=serializer_context)
        return Response(serializer.data , status=status.HTTP_201_CREATED)
