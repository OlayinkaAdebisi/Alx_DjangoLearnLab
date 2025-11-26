from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import book_list,CustomUser

admin.site.register(book_list)
admin.site.register(CustomUser)
