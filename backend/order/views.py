from django.shortcuts import get_object_or_404
from account.models.address import Address
from billing.models.payment import Payment
from store.models import Variety
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.generics import ListCreateAPIView , RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied , NotAcceptable
from django.utils.translation import ugettext_lazy as _
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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
            address = get_object_or_404(Address,uuid=address_id)
        except Exception as e:
            raise NotAcceptable("Please Enter an Address")

        try:
            payment_method = request.data["payment_method"]
        except Exception as e:
            raise NotAcceptable("Please Enter a payment_method")

        payment = Payment.objects.create(payment_method=payment_method)

        order = Order.objects.create(
            buyer=user,
            address=address,
            payment=payment
        )

        serializer_context={'request': request}
        serializer = OrderSerializer(order , context=serializer_context)
        return Response(serializer.data , status=status.HTTP_201_CREATED)

class OrderView(RetrieveDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "uuid"

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
            variety = orderRow.variety
            variety.inventory += orderRow.quantity
            variety.save()

        return Response({
            "detail": _("Order Canceled")
        } , status=status.HTTP_204_NO_CONTENT)

class OrderRowAPIView(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "uuid"

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

        if len(orderRows) > 20:
            raise NotAcceptable("If you want ordering more then 20 products, please send a ticket to us!")

        try:
            variety = get_object_or_404(Variety,uuid=request.data["variety"])
        except Exception as e:
            raise NotAcceptable("Please Enter a variety")

        current_item = OrderRow.objects.filter(order=order , variety=variety)

        if order.status != 0:
            raise NotAcceptable("You cannot add item to in process order")
        if variety.seller == user:
            raise PermissionDenied("This is Your variety")

        if len(current_item) > 0:
            raise NotAcceptable("You already have this item in your order")
        
        quantity = get_quantity_from_request(request , variety)
        
        order.total_price += quantity * variety.selling_price
        order.save()
        
        orderRow = OrderRow(order=order, variety=variety, quantity = quantity)
        orderRow.save()

        variety.inventory -= quantity
        variety.save()

        serializer_context={'request': request}
        serializer = OrderRowSerializer(orderRow , context=serializer_context)
        return Response(serializer.data , status=status.HTTP_201_CREATED)
