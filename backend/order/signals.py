from django.db.models.signals import post_save
from django.dispatch import receiver
from notice.sms_pannel_temp_codes import STORE_SELLER_NOTICE_NEW_ORDER

from notice.models import Notice
import json

from .models import *

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

