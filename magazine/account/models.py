from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.db import models

from account.managers import CustomUserManager


class User(AbstractUser):
    username = None
    phone = models.CharField(verbose_name='Phone', unique=True, max_length=30, blank=True)
    image = models.FileField(verbose_name='Image', upload_to='images/', blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
