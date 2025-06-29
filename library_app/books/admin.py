from django.contrib import admin
from .models import Book

# Register your models here.


# This will allow the Books model to be managed through the Django admin interface.
admin.site.register(Book)