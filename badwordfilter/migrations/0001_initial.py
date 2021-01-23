# Generated by Django 3.1.5 on 2021-01-23 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(help_text='Можете вписать любое слово - оно будет нормализовано автоматически', max_length=64, unique=True, verbose_name='Нормальная форма матерного слова')),
            ],
            options={
                'verbose_name': 'Матерное слово',
                'verbose_name_plural': 'Матерные слова',
            },
        ),
    ]