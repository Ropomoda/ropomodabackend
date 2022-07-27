from django.db import models

from app.models import TimeStampedModel


class CartItem(TimeStampedModel):
    class Meta:
        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"

    cart = models.ForeignKey('Cart',on_delete=models.CASCADE)
    product = models.ForeignKey('store.Product',on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.cart.id} {self.product.title_fa} {self.cart.profile.name}" 
