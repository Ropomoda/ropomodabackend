from datetime import timedelta
import time
from rest_framework.decorators import api_view
from rest_framework.response import Response

import random
from cache.tools import deleteKey, getKey, setKey
from utils.sms import send_sms
from .utils import *

@api_view(['POST'])
def login_activation_code(request):
    data = request.POST
    form_activation_code = data["activation_code"]
    phone_number = data["phone_number"]
    phone_number_cache_key_name = get_login_cache_key_name(phone_number)
    activation_code = str(getKey(phone_number_cache_key_name))
    if(form_activation_code == activation_code):
        deleteKey(phone_number_cache_key_name)
        return Response({
            "message": "login successfully",
        })
    else:
        return Response({
            "message": "login unsuccessfully",
        } , status=400)

@api_view(['POST'])
def send_activation_code(request):
    data = request.POST
    phone_number = data["phone_number"]
    phone_number_cache_key_name = get_login_cache_key_name(phone_number)


    if getKey(phone_number_cache_key_name):
        return Response({
            "message": "confirmation code sent 2 minutes before",
        })
    if(phone_number):
        activation_code = random.randint(10000 , 99999)
        setKey(phone_number_cache_key_name,activation_code, 60 * 2)
        send_sms(activation_code,phone_number)
    else:
        return Response({
            "message": "invalid input",
        })
    return Response({
        "message": "activation code sent successfully",
    })