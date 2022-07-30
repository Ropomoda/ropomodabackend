from django.db import models
from django.utils.translation import gettext_lazy  as _
from django.contrib.auth import get_user_model
from app.models import Extensions

User = get_user_model()

class Profile(Extensions):
    user = models.OneToOneField(to=User , on_delete=models.CASCADE)
    name = models.CharField(_('Name'),max_length=250 , default="کاربر روپومدا")
    national_id = models.IntegerField(null=True , blank=True)
    phone_number = models.CharField(max_length=25 ,null=True , blank=True)
    def __str__(self):
        return self.name