from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    """ Админка модели автора """
    list_display = ['id', 'name', 'surname', 'date_of_birth']


class BookAdmin(admin.ModelAdmin):
    """ Админка модели книги """
    list_display = ['id', 'correct_title', 'isbn', 'year_of_issue', 'pages_count', 'author']

    def correct_title(self, obj):
        return '"' + obj.title + '"'

    correct_title.short_description = 'title'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)