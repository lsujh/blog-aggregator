from django.contrib import admin

from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'title', 'message', 'files', 'created',)
    list_display_links = ('email',)
    ordering = ('-created',)


