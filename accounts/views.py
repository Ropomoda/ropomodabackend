from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from cache.tools import deleteKey, getKey, setKey
from utils.sms import  send_template_sms
from .utils import *
from django.contrib.auth import authenticate, login , get_user_model


User = get_user_model()


@api_view(['POST'])
def login_activation_code(request):
    data = request.POST
    if not 'phone_number' in data or not 'activation_code' in data:
        return Response(status=400)
    form_activation_code = data["activation_code"]
    phone_number = data["phone_number"]
    phone_number_cache_key_name = get_login_cache_key_name(phone_number)
    activation_code = str(getKey(phone_number_cache_key_name))

    if (form_activation_code == activation_code):
        if(User.objects.filter(phone_number=phone_number).exists()):
            user = User.objects.filter(phone_number=phone_number).first()
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
    if not 'phone_number' in data or not 'activation_code' in data:
        return Response({
            "message": "invalid input",
        },status=400)
    phone_number = data["phone_number"]
    phone_number_cache_key_name = get_login_cache_key_name(phone_number)
    if getKey(phone_number_cache_key_name):
        return Response({
            "message": "confirmation code sent 2 minutes before",
        })
    
    is_user_exist = User.objects.filter(phone_number=phone_number).exists()
    if(is_user_exist):
        activation_code = random.randint(10000 , 99999)
        setKey(phone_number_cache_key_name,activation_code, 60 * 2)
        send_template_sms([
            { "Parameter":"code" , "ParameterValue":activation_code }
        ], 
        activation_code,
        phone_number,
        '67586')
    else:
        pass
    return Response({
        "message": "activation code sent successfully",
    })

