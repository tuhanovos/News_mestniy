from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterFormView(UserCreationForm):
    email = forms.EmailField(max_length=254,
                             help_text='Это поле обязательно', widget=forms.TextInput(attrs={'placeholder': ''}))

    address = forms.CharField(max_length=100,
                              help_text='Укажите ваш город',
                              label='Ваш адрес', widget=forms.TextInput(attrs={'placeholder': ''}))

    password1 = forms.CharField(label="Пароль",
                                strip=False,
                                widget=forms.PasswordInput(attrs={'placeholder': ''}),
                                help_text='Введите ваш пароль')

    class Meta:
        model = User
        fields = ('username', 'email', 'address', 'password1', 'password2',)


class ProfileForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), max_length=150,
                            label='Заголовок новости')
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ''}), label='Текст новости')
