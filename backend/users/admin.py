from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from .models import User

TokenAdmin.raw_id_fields = ['user']


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name')
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
