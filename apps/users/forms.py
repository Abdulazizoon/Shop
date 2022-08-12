from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'username',
            'name': 'username',
            'placeholder': 'Логин'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'name': 'password',
            'placeholder': 'Введите пароль'
        }
    ))