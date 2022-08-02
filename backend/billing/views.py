
import json
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
from rest_framework.generics import CreateAPIView , RetrieveAPIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied , NotAcceptable
from rest_framework.permissions import IsAuthenticated
from django.conf import settings as conf_settings

from order.models.order import Order

MERCHANT = conf_settings.ZP_MERCHANT
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"


class PurchaseAPIView(CreateAPIView,RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Order.objects.all()
    lookup_field = "uuid"

    def post(self ,request , *args , **kwargs):
        user = self.request.user
        order = self.get_object()
        payment = order.payment
        if order.buyer != user:
            raise PermissionDenied("This order does not belong to you")

        if payment.is_payed:
            raise NotAcceptable("This order has purchased")

        if payment.payment_method == 1:
            raise NotAcceptable("This order payment method is COD")

        amount = order.total_price
        description = payment.description
        email = user.email
        mobile = user.mobile
        callbackURL = f'https://api.ropomoda.com/billing/purchase/order/{order.uuid}/'

        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "callback_url": callbackURL,
            "description": description,
            "metadata": {"mobile": mobile, "email": email}
        }
        req_header = {"accept": "application/json",
                    "content-type": "application/json'"}
        req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
            req_data), headers=req_header)
        authority = req.json()['data']['authority']
        if len(req.json()['errors']) == 0:
            payment.authority = authority
            payment.save()
            return Response({
                "payment_url": ZP_API_STARTPAY.format(authority=authority)
            })
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return Response({
                "detail":f"Error code: {e_code}, Error Message: {e_message}"
            })

    def get(self ,request , *args , **kwargs):
        user = self.request.user
        order = self.get_object()
        payment = order.payment

        amount = order.total_price

        t_status = request.GET.get('Status')
        t_authority = request.GET['Authority']
        if request.GET.get('Status') == 'OK':
            req_header = {"accept": "application/json",
                        "content-type": "application/json'"}
            req_data = {
                "merchant_id": MERCHANT,
                "amount": amount,
                "authority": t_authority
            }
            req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
            if len(req.json()['errors']) == 0:
                t_status = req.json()['data']['code']
                if t_status == 100:
                    if payment.authority == t_authority and not payment.is_payed:
                        payment.ref_id = req.json()['data']['ref_id']
                        payment.status = 2
                        payment.is_payed = True
                        payment.save()
                    else:
                        return HttpResponse("invalid order id or authority ")

                    return redirect(f"https://www.ropomoda.com/user/order/{order.uuid}/?payment_status=100")

                elif t_status == 101:
                    return redirect(f"https://www.ropomoda.com/user/order/{order.uuid}/?payment_status=101")
                else:
                    return HttpResponse('Transaction failed.\nStatus: ' + str(
                        req.json()['data']['message']
                    ))

            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
        else:
            return HttpResponse('Transaction failed or canceled by user')