from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterFormView(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')
    address = forms.CharField(max_length=100, help_text='Укажите ваш город', label='Ваш адрес')

    class Meta:
        model = User
        fields = ('username', 'email', 'address', 'password1', 'password2',)

