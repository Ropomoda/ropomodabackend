from django.db import models

from app.models import Extensions

class OrderRow(Extensions):
    class Meta:
        verbose_name = "OrderRow"
        verbose_name_plural = "OrderRows"

    order = models.ForeignKey('Order',on_delete=models.CASCADE)
    variety = models.ForeignKey('store.Variety',on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @staticmethod
    def get_all_order_rows_od_order():
        return OrderRow.objects.all()
    def __str__(self):
        return f"{self.order.id} {self.variety.product.title_fa} {self.order.buyer.name}" 
