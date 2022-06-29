from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy  as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=200)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    auth_code = models.CharField(max_length=200)
    objects = CustomUserManager()

    def __str__(self):
        return self.email
