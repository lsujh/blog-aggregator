from django.contrib import admin

from .models import News, Urls, StopWords


class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("News", {"fields": ["title", "link", "published"]}),
        ("DB Dates", {"fields": ["created_at, updated_at"]}),
        ("Source", {"fields": ["source"]}),
    ]

admin.site.register(News, NewsAdmin)
admin.site.register(Urls)
admin.site.register(StopWords)
