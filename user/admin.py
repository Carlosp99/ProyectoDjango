from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUseradmin
from user.models import User

@admin.register(User)
class UserAdmin(BaseUseradmin):
    fieldsets = (
        (None, {'fields':('username', 'password')}),
        ('Informacion Personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Redes sociales', {'fields': ('web_site', 'twitter')})
    )