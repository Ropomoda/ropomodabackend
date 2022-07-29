from django.db.models.signals import post_save
from django.dispatch import receiver
from notice.sms_pannel_temp_codes import STORE_CUSTOMER_NOTICE_ORDER_INITIATED, STORE_SELLER_NOTICE_NEW_ORDER

from notice.models import Notice
import json

from .models import *
from account.models import Profile

@receiver(post_save, sender=OrderRow)
def send_order_notification_to_seller(sender, instance, created, **kwargs):
    if created:
        payload = json.dumps([
            { "Parameter":"name" , "ParameterValue": instance.product.seller.store_name}
        ])
        
        Notice.objects.create(to=instance.product.seller.user , 
            type_code=STORE_SELLER_NOTICE_NEW_ORDER ,
            should_send_sms=True ,
            body=payload
        )

@receiver(post_save, sender=Order)
def send_order_notification_to_customer(sender, instance, created, **kwargs):
    if created:
        profile = Profile. objects.get(user=instance.buyer)
        tracking_code = str(instance.id)[:8]
        payload = json.dumps([
            { "Parameter":"name" , "ParameterValue": profile.name},
            { "Parameter":"code" , "ParameterValue": tracking_code},
            { "Parameter":"link" , "ParameterValue": f'ropomoda.com/t/{tracking_code}'},
        ])
        
        Notice.objects.create(to=instance.buyer , 
            type_code=STORE_CUSTOMER_NOTICE_ORDER_INITIATED,
            should_send_sms=True ,
            body=payload
        )
