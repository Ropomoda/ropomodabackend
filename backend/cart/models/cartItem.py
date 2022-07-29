from django.db import models

from app.models import Extensions


class CartItem(Extensions):
    class Meta:
        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"

    cart = models.ForeignKey('Cart',on_delete=models.CASCADE)
    product = models.ForeignKey('store.Product',on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.cart.user.mobile} {self.product.title_fa}" 
