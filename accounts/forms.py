from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student


class RegisterForm(UserCreationForm):
    avatar = forms.FileField(
        required=False,
        label=False
    )

    username = forms.CharField(
        max_length=200,
        required=True,
        label='Имя пользователя',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
    )

    email = forms.EmailField(
        max_length=100,
        required=False,
        label='Адрес электронной почты',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Адрес электронной почты'}),
    )

    password1 = forms.CharField(
        required=True,
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
    )

    password2 = forms.CharField(
        required=True,
        label='Повторите пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),
    )

    check = forms.BooleanField(
        required=True,
        label='Я подтверждаю',
    )

    class Meta:
        model = User
        fields = [
            'avatar', 'username', 'email', 'password1', 'password2', 'check',
        ]
