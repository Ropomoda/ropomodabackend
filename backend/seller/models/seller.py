
from django.db import models

from seller.utils import seller_logo_path
from app.models import BaseUUIDModel

class Seller(BaseUUIDModel):
    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"
        
    profile = models.ForeignKey('account.Profile' , on_delete=models.CASCADE)
    store_name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to=seller_logo_path , null=True , blank=True, default=None)

    def __str__(self) -> str:
        return f'{self.store_name}'