from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from magazine import settings


class RegisterForm(UserCreationForm):
    pass


class EditUserForm(UserChangeForm):
    class Meta:
        models = settings.AUTH_USER_MODEL
        fields = '__all__'
        # fields = ['first_name', 'last_name', 'phone', 'image']





class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
