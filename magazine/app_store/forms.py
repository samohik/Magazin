from django import forms
from django.forms import ModelForm

from app_store.models import Tags


class SortForm(forms.Form):
    SORT_CHOICES = (
        ("price", "Price: low to high"),
        ("-price", "Price: high to low"),
        ("sold", "Popular: low to high"),
        ("-sold", "Popular: high to low"),
        ("-review", "Reviews: low to high"),
        ("review", "Reviews: high to low"),
        ("updated", "New: low to high"),
        ("-updated", "New: high to low"),
    )
    choices = forms.ChoiceField(choices=SORT_CHOICES, required=False)


class TagsForm(ModelForm):

    class Meta:
        model = Tags
        fields = ['name']


class ReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
