from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # Show these fields in list view
    search_fields = ('title', 'author')                      # Add search box for title & author
    list_filter = ('publication_year',)                      # Add filter sidebar for publication year
