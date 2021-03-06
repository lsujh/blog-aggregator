# Generated by Django 3.1.5 on 2021-01-23 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bookmark", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookmarkcomment",
            name="obj",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="comments.comment",
                verbose_name="Коментар",
            ),
        ),
        migrations.AddField(
            model_name="bookmarkcomment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Користувач",
            ),
        ),
    ]
