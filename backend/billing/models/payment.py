from django.db import models
from app.models import Extensions
from django.contrib.auth import get_user_model

User = get_user_model()

class Payment(Extensions):
    description = models.TextField(max_length=200 , null=True , blank=True , default="خرید از وبسایت روپومدا")
    authority = models.CharField(max_length=250 ,null=True , blank=True)
    PAYMENT_STATUSES = (
        (0 , "INITIATED"),
        (1 , "PENDING"),
        (2 , "SUCCESS"),
        (4 , "CANCELED"),
        (5 , "FAILED"),
    )

    status = models.IntegerField(choices=PAYMENT_STATUSES , default=0)

    PAYMENT_METHOD_CHOICES = (
        (0 , "ZARRIN_PAL"),
        (1 , "COD"),
    )

    payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES)
    ref_id = models.TextField(max_length=250 ,null=True , blank=True)
    is_payed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.uuid} {self.authority}'