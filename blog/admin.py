from mptt.admin import TreeRelatedFieldListFilter, MPTTModelAdmin

from django.contrib import admin

from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = (
        "name",
        "slug",
        "parent",
        "id",
    )
    list_display_links = ("slug",)
    list_filter = (("parent", TreeRelatedFieldListFilter),)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "publish", "status")
    list_filter = ("status", "created", "publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("status", "publish")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
