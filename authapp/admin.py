from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import MyUser


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'role', 'is_staff', 'is_superuser', 'is_active', 'last_login']


admin.site.register(Permission)
