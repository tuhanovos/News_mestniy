# Generated by Django 2.1 on 2018-09-09 12:25

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCreateNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок новости')),
                ('news_text', ckeditor.fields.RichTextField(verbose_name='Текст новости')),
                ('news_date', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]