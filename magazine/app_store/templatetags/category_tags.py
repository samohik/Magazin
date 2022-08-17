from django import template
from app_store.models import *


register = template.Library()


@register.simple_tag()
def get_category(row_id=None):
    if not row_id:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=row_id)


@register.inclusion_tag('app_store/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cat = Category.objects.all()
    else:
        cat = Category.objects.order_by(sort)
    return {'cat': cat, 'cat_selected': cat_selected}


@register.inclusion_tag('app_store/sort_product.html')
def sort_product(sort=None):
    items = Items.objects.all()
    return {'items': items}
