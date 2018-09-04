from ckeditor.fields import RichTextField
from django.db import models

""" 
En: This is the model news
Rus: Модель новости
"""


class UserCreateNews(models.Model):
    title = models.CharField(max_length=100, name='title', verbose_name='Заголовок новости')
    news_text = models.TextField(name='news_text', verbose_name='Текст новости')
    news_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

