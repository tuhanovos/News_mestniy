# Generated by Django 2.1 on 2018-09-16 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriesnews',
            options={'verbose_name': 'Категория новостей', 'verbose_name_plural': 'Категории новостей'},
        ),
        migrations.AlterField(
            model_name='usercreatenews',
            name='categories_news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.CategoriesNews', verbose_name='Категория'),
        ),
    ]
