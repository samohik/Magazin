import django_filters

from .models import Manufacturer, Items, Characteristic


class ItemsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.RangeFilter()
    manufacture = django_filters.ModelChoiceFilter(
        queryset=Manufacturer.objects.all())

    character = django_filters.ModelChoiceFilter(
        queryset=Characteristic.objects.all())

    class Meta:
        model = Items
        fields = [
            'price',
            'manufacture',
            'character',
        ]
