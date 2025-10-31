from django.contrib import admin
from .models import Book
# Register your models here.
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')
    search_fields = ('title', 'author','published_year')
    list_filter = ('status', 'due_back')