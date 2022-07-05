from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy  as _

from .managers import UserManager


class User(AbstractUser):
    username = None
    phone_number = models.CharField(_('phone number'), unique=True , max_length=20 , null=True , blank=True)

    name = models.CharField(max_length=200 , null=True , blank=True)
    email = models.EmailField(_('email address') , null=True , blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    mobile_is_verified = models.BooleanField(default=False)
    email_is_verified = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.phone_number

class Profile(models.Model):
    user = models.OneToOneField('User' , on_delete=models.PROTECT , primary_key=True)
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.user.phone_number