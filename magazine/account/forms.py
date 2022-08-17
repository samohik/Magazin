from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User

from account.models import Profile


class RegisterForm(UserCreationForm):
    pass


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = User


class EditUserForm(UserChangeForm):
    phone = forms.CharField(max_length=20)
    image = forms.FileField(disabled=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileUserForm:
    class Meta:
        model = Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
