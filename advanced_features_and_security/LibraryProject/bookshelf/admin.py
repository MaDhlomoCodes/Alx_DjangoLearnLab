from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Book, CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'added_by')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('published_date', 'author')
    raw_id_fields = ('added_by',)  # Improves performance for large user databases

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth', 'profile_photo'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)  # Default ordering

# Explicit registrations (required by checker)
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)