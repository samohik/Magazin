from django.db import models
from django.urls import reverse

from account.models import User


class Items(models.Model):
    name = models.CharField(verbose_name='Name', max_length=120)
    image = models.ImageField(verbose_name='Image', upload_to='product')
    description = models.TextField(verbose_name='Description')
    price = models.PositiveIntegerField(verbose_name='Price')
    count = models.PositiveIntegerField(verbose_name='Count', default=1)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,  blank=True, null=True)
    manufacture = models.ForeignKey('Manufacturer', blank=True, null=True, related_name='item', on_delete=models.CASCADE)
    sold = models.PositiveIntegerField(verbose_name='Sold', default=0, blank=True)
    available = models.BooleanField(verbose_name='Published', default=False, blank=True)
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('store:product_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'


class Manufacturer(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'manufacturer'
        verbose_name_plural = 'manufacturers'


class ItemsTag(models.Model):
    item = models.ForeignKey('Items', related_name='tags', on_delete=models.CASCADE, blank=True)
    tags = models.ForeignKey('Tags', related_name='tags', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return str(self.tags)


class Tags(models.Model):
    name = models.CharField(verbose_name='Tag name', max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class Status(models.Model):
    name = models.CharField(verbose_name='Status', max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'status'


class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)

    def get_absolute_url(self):
        return reverse('store:category', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'category\'s'


class Characteristic(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, related_name='character', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Tag', max_length=150, blank=True)

    def __str__(self):
        return str(self.name)


class Reviews(models.Model):
    profile = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE, null=True)
    item = models.ForeignKey('Items', related_name='review', on_delete=models.CASCADE, null=True)
    text = models.TextField(verbose_name='Review')
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True)

    def __str__(self):
        return str(self.created)

    class Meta:
        ordering = ['-updated']
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
