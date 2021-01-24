from mptt.models import TreeForeignKey, MPTTModel
from meta.models import ModelMeta
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models, IntegrityError
from django.utils import timezone

from comments.models import Comment
from likes.models import LikeDislike
from config.fields import ListField
from .managers import PublishedManager

CustomUser = get_user_model()

class Tag(models.Model):
    name = models.CharField("Тег", max_length=50, unique=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name

class Category(MPTTModel):
    parent = TreeForeignKey(
        "self",
        verbose_name="Батьківська категорія",
        related_name="children",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    name = models.CharField("Назва", db_index=True, max_length=200)
    description = models.TextField(verbose_name="Опис", blank=True, null=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    published = models.BooleanField('Опубліковано', default=True)

    class MPTTMeta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:post_list", args=[self.slug],)

    @property
    def items_count(self):
        ids = self.get_descendants(include_self=True).values_list("id")
        return Post.published.filter(category_id__in=ids).count()


class Post(ModelMeta, models.Model):
    STATUS_CHOICES = (
        ("draft", "Чорновик"),
        ("published", "Опубліковано"),
    )
    category = TreeForeignKey(
        "Category",
        related_name="posts",
        on_delete=models.CASCADE,
        verbose_name="Категорія",
    )
    title = models.CharField(verbose_name="Назва", max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, db_index=True, unique=True, blank=True)
    description = RichTextUploadingField(verbose_name="Опис", blank=True)
    body = RichTextUploadingField(verbose_name="Стаття")
    status = models.CharField(
        max_length=10, verbose_name="Статус", choices=STATUS_CHOICES, default="draft"
    )
    publish = models.DateTimeField(verbose_name="Дата публікації", default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    keywords = ArrayField(models.CharField(max_length=50), blank=True,
                          verbose_name="Ключові слова", help_text='A comma-separated list of keywords.')
    author = models.ForeignKey(
        CustomUser, verbose_name="Автор", on_delete=models.CASCADE, related_name="post_author"
    )
    comments = GenericRelation(Comment, related_query_name="post_comment")
    likes = GenericRelation(LikeDislike, related_query_name='post_likes')
    tags = models.ManyToManyField(Tag, verbose_name="Тег", blank=True)
    source = models.CharField('Джерело', max_length=100, blank=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"
        ordering = ("-publish",)
        index_together = (("id", "title"),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[self.category.slug, self.slug,],
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{timezone.now().year}-{timezone.now().month}-{timezone.now().day}-{slugify(self.title)}"
        try:
            super(self.__class__, self).save(*args, **kwargs)
        except IntegrityError:
            self.slug = f"{timezone.now().year}-{timezone.now().month}-{timezone.now().day}-{timezone.now().hour}-" \
                        f"{timezone.now().minute}-{slugify(self.title)}"
            super(self.__class__, self).save(*args, **kwargs)


    _metadata = {
        "title": "title",
        "description": "description",
        "keywords": "keywords",
        'publisher': 'author',
        'author': 'author',
    }

    def get_bookmark_count(self):
        return self.bookmarkpost_set.all().count()


class PostStatistic(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_views')
    date = models.DateField("Дата", default=timezone.now)
    views = models.IntegerField("Перегляди", default=0)

    def __str__(self):
        return self.post.title
