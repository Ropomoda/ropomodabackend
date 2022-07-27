from django.db import models
from django.utils.translation import gettext_lazy  as _

from app.models import BaseUUIDModel


class Profile(BaseUUIDModel):
    user = models.ForeignKey('account.User' , on_delete=models.CASCADE)
    name = models.CharField(_('Name'),max_length=250 , default="کاربر روپومدا")
    def __str__(self):
        return self.name