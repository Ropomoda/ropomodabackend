import django
from django.db import models

from app.models import Extensions
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(Extensions):
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    buyer = models.ForeignKey(to=User , on_delete=models.CASCADE )
    STATUS_CHOICES = (
        (0 , "INITIATED"),
        (3 , "ACCEPTED_PROCESSING"),
        (6 , "DELIVERED_POSTOFFICE"),
        (9 , "DELIVERY_POSTMAN"),
        (11 , "DELIVERY_CUSTOMER"),
        (12 , "CANCELED_BY_USER"),
        (13 , "CANCELED_BY_SELLER"),
        (14 , "CANCELED_BY_ADMIN"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES , default=0)
    PAYMENT_METHOD_CHOICES = (
        (0 , "ZARRIN_PAL"),
        (1 , "COD"),
    )
    address = models.ForeignKey('account.Address' , on_delete=models.CASCADE)
    payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES)
    is_payed = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.uuid} {self.buyer.mobile}" 

