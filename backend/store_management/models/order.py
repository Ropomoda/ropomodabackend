from pyexpat import model
from django.db import models


class Order(models.Model):
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    user = models.ForeignKey(to='accounts.Profile' , on_delete=models.CASCADE )

    STATUS_CHOICES = (
        (0 , "INITIATED"),
        (1 , "ACCEPTED_PROCESSING"),
        (2 , "DELIVERED_POSTOFFICE"),
        (3 , "DELIVERY_AGENT_SENT"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES)
    PAYMENT_METHOD_CHOICES = (
        (0 , "ZARRIN_PAL"),
        (1 , "COD"),
    )
    payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.BooleanField(default=False)

    @staticmethod
    def get_all_orders_of_user():
        return Order.objects.all()
    def __str__(self):
        return f"{ self.id} {self.user.name}" 

class OrderRow(models.Model):
    class Meta:
        verbose_name = "OrderRow"
        verbose_name_plural = "OrderRows"

    order = models.ForeignKey('Order',on_delete=models.CASCADE )
    product = models.ForeignKey('Product',on_delete=models.CASCADE )
    count = models.IntegerField()

    @staticmethod
    def get_all_order_rows_od_order():
        return OrderRow.objects.all()
    def __str__(self):
        return f"{self.order.id} {self.product.name} {self.order.user.name}" 
