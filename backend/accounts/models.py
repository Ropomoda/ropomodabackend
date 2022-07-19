from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy  as _

from .managers import UserManager


class User(AbstractUser):
    username = None
    mobile = models.CharField(_('phone number'), unique=True , max_length=20 , null=True , blank=True)

    name = models.CharField(max_length=200 , null=True , blank=True)
    email = models.EmailField(_('email address') , null=True , blank=True)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    mobile_verified = models.BooleanField(default=False)
    email_is_verified = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.mobile

class Profile(models.Model):
    user = models.ForeignKey('User' , on_delete=models.CASCADE  )
    name = models.CharField(_('Name'),max_length=250 , default="کاربر روپومدا")
    def __str__(self):
        return self.name