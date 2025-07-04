from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'full_name', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'full_name', 'email')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'email','job','image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, CustomUserAdmin)
