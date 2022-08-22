from django.contrib import admin

from app_store.models import *


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'created', 'updated']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ItemsTag)
class ItemsTagAdmin(admin.ModelAdmin):
    list_display = ['item', 'tags']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['name']
