from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
