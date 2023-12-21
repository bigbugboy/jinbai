from django.contrib import admin


from . import models


class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

class SingleChoiceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'no', 'tag', 'star', 'status', 'updated_at']
    search_fields = ['pk', 'no', 'status', 'star']
    search_help_text = '支持搜索的字段: pk/no/star/status'
    



admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.SingleChoice, SingleChoiceAdmin)
