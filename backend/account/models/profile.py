from django.db import models
from django.utils.translation import gettext_lazy  as _
from django.contrib.auth import get_user_model
from app.models import BaseUUIDModel

User = get_user_model()

class Profile(BaseUUIDModel):
    user = models.OneToOneField(to=User , on_delete=models.CASCADE)
    name = models.CharField(_('Name'),max_length=250 , default="کاربر روپومدا")
    def __str__(self):
        return self.name