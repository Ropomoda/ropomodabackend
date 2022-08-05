# notice/tasks.py

from celery import shared_task

from utils.sms import send_template_sms

@shared_task()
def send_notice_sms_task(payload, mobile , type_code):
    """Sends notice sms"""
    print("task")
    send_template_sms(payload,mobile,type_code)

