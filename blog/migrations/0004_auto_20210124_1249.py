# Generated by Django 3.1.5 on 2021-01-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210124_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='source',
            field=models.CharField(blank=True, max_length=100, verbose_name='Джерело'),
        ),
    ]
