# Generated by Django 2.1 on 2018-09-11 16:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercreatenews',
            name='news_text',
        ),
        migrations.AlterField(
            model_name='usercreatenews',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст новости'),
        ),
    ]