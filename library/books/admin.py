from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug')
    list_display_links = ('title',)
    search_fields = ('title', 'author', 'description')
    list_filter = ('author',)
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'description', 'slug')
        }),
    )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Book, BookAdmin)
