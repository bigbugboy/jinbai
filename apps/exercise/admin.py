from django.contrib import admin


from . import models


class SingleChoiceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'star', 'status', 'title']



admin.site.register(models.Tag)
admin.site.register(models.SingleChoice, SingleChoiceAdmin)
