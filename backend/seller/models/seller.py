
from django.db import models


class Seller(models.Model):
    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"
        
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to="images/seller/")