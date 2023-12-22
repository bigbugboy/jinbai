from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'telephone', 'vip']
    search_fields = ['username', 'telephone']



admin.site.register(User, UserAdmin)