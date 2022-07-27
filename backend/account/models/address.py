from django.db import models
from django.utils.translation import gettext_lazy  as _

from app.models import Extensions


class Address(Extensions):
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    profile = models.ForeignKey('account.Profile' , on_delete=models.CASCADE  )
    name = models.CharField(_('Name'),max_length=250 , default="" , null=True, blank=True)
    description = models.TextField(default="" , null=True, blank=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15)
    latitude = models.DecimalField(max_digits=30, decimal_places=15)

    state = models.CharField(_('State'),max_length=100)
    city = models.CharField(_('City'),max_length=100)
    post_address = models.TextField(_('Post Address'))
    plaque = models.IntegerField()
    floor = models.IntegerField(null=True , default=0 , blank=True)
    post_code = models.CharField(max_length=20)
    
    def __str__(self):
        return self.profile.name