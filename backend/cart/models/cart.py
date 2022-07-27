from django.db import models

from app.models import BaseUUIDModel


class Cart(BaseUUIDModel):
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    profile = models.OneToOneField(to='account.Profile' , on_delete=models.CASCADE )

    def __str__(self):
        return f"{self.profile.name} {self.profile.user.mobile}" 

