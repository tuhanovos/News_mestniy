from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

""" 
En: This is the model of the user profile in which he adds the news
Rus: Это модель профиля пользователя в которой он добавляет новость
"""


class UserCreateNews(models.Model):
    title = models.CharField(max_length=100, name='title', verbose_name='Заголовок новости')
    news_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    news_image = models.ImageField(verbose_name='Изображение', null=True, blank=True, upload_to='images/')
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Текст новости')

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

