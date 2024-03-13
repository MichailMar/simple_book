from django.contrib import admin

from .models import Book, BookBorrow, User, Dept

admin.site.register(Book)
admin.site.register(BookBorrow)
admin.site.register(User)
admin.site.register(Dept)
