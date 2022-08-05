import json
from django.db.models.signals import post_save
from django.dispatch import receiver
import json
from notice.tasks import send_notice_sms_task

from .models import Notice

@receiver(post_save, sender=Notice)
def send_notifications_request(sender, instance, created, **kwargs):
    if instance.should_send_sms:
        payload = json.loads(instance.body)
        send_notice_sms_task.delay(payload, instance.to.mobile, instance.type_code)
