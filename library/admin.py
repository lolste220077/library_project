from django.contrib import admin
from .models import Book, Reader

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'quantity')
    search_fields = ('title', 'author')

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'group_number', 'phone')
    search_fields = ('full_name',)