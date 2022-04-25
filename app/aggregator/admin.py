from django.contrib import admin

from .models import Log, LogFile


class LogAdmin(admin.ModelAdmin):
    """Админка логов"""
    list_display_links = ['id', 'ip', ]
    list_display = ['id', 'ip', 'url', 'method', 'status']
    list_filter = ['ip', 'method', 'status']
    list_per_page = 100
    date_hierarchy = 'time'


class TestLogAdmin(admin.ModelAdmin):
    list_display_links = ['id', ]
    list_display = ['id', 'row']


class LogFileAdmin(admin.ModelAdmin):
    list_display_links = ['id', ]
    list_display = ['id', 'file', 'processed']
    readonly_fields = ['processed']


# admin.site.register(TestLog, TestLogAdmin)

admin.site.register(Log, LogAdmin)
admin.site.register(LogFile, LogFileAdmin)
