from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'telephone', 'vip', 'vip_type', 'vip_end_date']
    search_fields = ['username', 'telephone']



admin.site.register(User, UserAdmin)