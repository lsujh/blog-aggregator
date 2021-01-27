from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    link = models.CharField('Посилання', max_length=2083, default="", unique=True)
    category = models.CharField('Категорія', max_length=250, blank=True)
    description = models.TextField('Короткий опис', blank=True)
    published = models.DateTimeField('Опубліковано')
    created_at = models.DateTimeField('Отримано', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    source = models.CharField('Джерело', max_length=30, default="", blank=True, null=True)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


class Urls(models.Model):
    url = models.URLField()
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.url


class StopWords(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word
