from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('nonce', 'message_user_id')}),)
    list_display = ['username', 'email', 'nonce', 'message_user_id']


admin.site.register(User, UserAdmin)
