from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.db import models

from account.managers import CustomUserManager


phone_validator = RegexValidator("\d{3}\-?\d{2}\-?\d{3}\-?\d{2}\-?\d{2}", "Phone format needs to be +___-__-___-__-__.")


def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')


class User(AbstractUser):
    username = None
    phone = models.CharField(verbose_name='Phone', validators=[phone_validator], unique=True, max_length=30, blank=True)
    image = models.FileField(verbose_name='Image', validators=[file_size], upload_to='images/', blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
