from django.db import models

from app.models import BaseUUIDModel


class Order(BaseUUIDModel):
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    buyer = models.ForeignKey(to='account.Profile' , on_delete=models.CASCADE )

    STATUS_CHOICES = (
        (0 , "INITIATED"),
        (1 , "ACCEPTED_PROCESSING"),
        (2 , "DELIVERED_POSTOFFICE"),
        (3 , "DELIVERY_AGENT_SENT"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES , default=0)
    PAYMENT_METHOD_CHOICES = (
        (0 , "ZARRIN_PAL"),
        (1 , "COD"),
    )
    address = models.ForeignKey('account.Address' , on_delete=models.CASCADE)
    payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES)
    is_payed = models.BooleanField(default=False)

    @staticmethod
    def init():
        pass
    @staticmethod
    def get_all_orders_of_user():
        return Order.objects.all()
    def __str__(self):
        return f"{ self.id} {self.buyer.name}" 

