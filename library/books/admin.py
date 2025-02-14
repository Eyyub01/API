from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'slug')
    list_display_links = ('title',)
    search_fields = ('title', 'author', 'description')
    list_filter = ('published_date', 'author')
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'description', 'published_date', 'slug')
        }),
    )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Book, BookAdmin)
