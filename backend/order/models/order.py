from django.db import models

from app.models import Extensions


class Order(Extensions):
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
    payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES)
    is_payed = models.BooleanField(default=False)

    @staticmethod
    def get_all_orders_of_user():
        return Order.objects.all()
    def __str__(self):
        return f"{ self.uuid} {self.buyer.name}" 

