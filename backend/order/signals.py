from django.db.models.signals import post_save
from django.dispatch import receiver
from notice.consts import STORE_CUSTOMER_NOTICE_ORDER_DELIVERED_CUSTOMER, STORE_CUSTOMER_NOTICE_ORDER_DELIVERED_POST_OFFICE, STORE_CUSTOMER_NOTICE_ORDER_DELIVERED_POSTMAN, STORE_CUSTOMER_NOTICE_ORDER_INITIATED, STORE_SELLER_NOTICE_NEW_ORDER

from notice.models import Notice
import json

from .models import *
from account.models import Profile

@receiver(post_save, sender=OrderRow)
def send_order_notification_to_seller(sender, instance, created, **kwargs):
    if created:
        payload = json.dumps([
            { "Parameter":"name" , "ParameterValue": instance.variety.seller.store_name}
        ])
        
        Notice.objects.create(to=instance.variety.seller.user , 
            type_code=STORE_SELLER_NOTICE_NEW_ORDER ,
            should_send_sms=True ,
            body=payload
        )

@receiver(post_save, sender=Order)
def send_order_notification_to_customer(sender, instance, created, **kwargs):
    profile = Profile. objects.get(user=instance.buyer)
    tracking_code = str(instance.uuid)[:8]

    if created:
        payload = json.dumps([
            { "Parameter":"name" , "ParameterValue": profile.name},
            { "Parameter":"code" , "ParameterValue": tracking_code},
            { "Parameter":"link" , "ParameterValue": f'rpmd.ir/t/{tracking_code}'},
        ])
        
        Notice.objects.create(to=instance.buyer , 
            type_code=STORE_CUSTOMER_NOTICE_ORDER_INITIATED,
            should_send_sms=True ,
            body=payload
        )
    elif instance.status == 6:
        payload = json.dumps([
            { "Parameter":"name" , "ParameterValue": profile.name},
            { "Parameter":"transfererName" , "ParameterValue": "پست"},
            { "Parameter":"code" , "ParameterValue": tracking_code},
            { "Parameter":"link" , "ParameterValue": f'rpmd.ir/t/{tracking_code}'},
        ])
        
        Notice.objects.create(to=instance.buyer , 
            type_code=STORE_CUSTOMER_NOTICE_ORDER_DELIVERED_POST_OFFICE,
            should_send_sms=True ,
            body=payload
        )
    elif instance.status == 9:
        payload = json.dumps([
            { "Parameter":"name" , "ParameterValue": profile.name},
            { "Parameter":"code" , "ParameterValue": tracking_code},
            { "Parameter":"link" , "ParameterValue": f'rpmd.ir/t/{tracking_code}'},
        ])
        
        Notice.objects.create(to=instance.buyer , 
            type_code=STORE_CUSTOMER_NOTICE_ORDER_DELIVERED_POSTMAN,
            should_send_sms=True ,
            body=payload
        )
    elif instance.status == 11:
        payload = json.dumps([
            { "Parameter":"name" , "ParameterValue": profile.name},
            { "Parameter":"code" , "ParameterValue": tracking_code},
            { "Parameter":"link" , "ParameterValue": f'rpmd.ir/t/{tracking_code}'},
        ])
        
        Notice.objects.create(to=instance.buyer , 
            type_code=STORE_CUSTOMER_NOTICE_ORDER_DELIVERED_CUSTOMER,
            should_send_sms=True ,
            body=payload
        )