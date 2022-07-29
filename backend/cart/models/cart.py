from django.db import models

from app.models import Extensions
from django.contrib.auth import get_user_model

User = get_user_model()

class Cart(Extensions):
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    user = models.OneToOneField(to=User , on_delete=models.CASCADE )

    def __str__(self):
        return f"{self.user.mobile}" 

