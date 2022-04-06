from django.contrib import admin

from .models import Log


class LogAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'ip',]
    list_display = ['id', 'ip', 'url', 'method', 'code']
    list_filter = ['ip', 'method', 'code']


admin.site.register(Log, LogAdmin)
