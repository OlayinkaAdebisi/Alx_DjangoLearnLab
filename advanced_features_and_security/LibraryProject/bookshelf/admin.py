from django.contrib import admin
from .models import Book,CustomUser
from django.contrib.auth.admin import UserAdmin


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author','publication_year')
    list_filter = ('title', 'author','publication_year')
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "date_of_birth", "profile_photo"]
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = [
        (None, {"fields": ["username", "password"]}),
        ("Personal info", {"fields": ["email","profile_photo","date_of_birth"]}),
        ("Permissions", {"fields": ["is_staff","is_superuser"]}),
    ]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2'),
        }),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
# Register your models here.

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)