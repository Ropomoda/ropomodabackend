from django.db import models

from app.models import Extensions


class CartItem(Extensions):
    class Meta:
        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"

    cart = models.ForeignKey('Cart',on_delete=models.CASCADE)
    variety = models.ForeignKey('store.Variety',on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.cart.user.mobile} {self.product.title_fa}" 
