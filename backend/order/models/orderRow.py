from django.db import models

from app.models import TimeStampedModel


class OrderRow(TimeStampedModel):
    class Meta:
        verbose_name = "OrderRow"
        verbose_name_plural = "OrderRows"

    order = models.ForeignKey('Order',on_delete=models.CASCADE)
    product = models.ForeignKey('store.Product',on_delete=models.CASCADE)
    count = models.IntegerField()

    @staticmethod
    def get_all_order_rows_od_order():
        return OrderRow.objects.all()
    def __str__(self):
        return f"{self.order.id} {self.product.title_fa} {self.order.buyer.name}" 
