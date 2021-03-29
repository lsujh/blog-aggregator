# Generated by Django 3.1.5 on 2021-01-26 12:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0002_auto_20210125_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='StopWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), help_text='A comma-separated list of word.', size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('description', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-published',)},
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(blank=True, max_length=250, verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Отримано'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(blank=True, verbose_name='Короткий опис'),
        ),
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.CharField(default='', max_length=2083, unique=True, verbose_name='Посилання'),
        ),
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(verbose_name='Опубліковано'),
        ),
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Джерело'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]