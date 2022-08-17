from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name='User', related_name='profile', on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Phone', max_length=30, blank=True)
    image = models.FileField(verbose_name='Image', upload_to='images/', blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
