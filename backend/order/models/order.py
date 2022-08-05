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
        (-3 , "CANCELED_BY_ADMIN"),
        (-2 , "CANCELED_BY_SELLER"),
        (-1 , "CANCELED_BY_USER"),
        (0 , "INITIATED"),
        (1 , "REGISTERED"),
        (2 , "PROCESSING"),
        (6 , "DELIVERED_POSTOFFICE"),
        (9 , "DELIVERY_POSTMAN"),
        (11 , "DELIVERY_CUSTOMER"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES , default=0)
    
    total_price = models.IntegerField(default=0)
   
    address = models.ForeignKey('account.Address' , on_delete=models.CASCADE)
    payment = models.ForeignKey('billing.Payment' , on_delete=models.CASCADE , default=None)
    is_closed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.uuid} {self.buyer.mobile}" 

