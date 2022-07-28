from django.db import models

from app.models import BaseUUIDModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Cart(BaseUUIDModel):
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    user = models.OneToOneField(to=User , on_delete=models.CASCADE )

    def __str__(self):
        return f"{self.user.mobile} {self.user.mobile}" 

