from django.db import models
from django.conf import settings


class LogFile(models.Model):
    file = models.FilePathField(path=settings.LOG_PATH, match=r".*\.log$")
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'


class TestLog(models.Model):
    row = models.CharField(max_length=600, help_text='User-agent')

    def __str__(self):
        return f'{self.id}'


class Log(models.Model):
    ip = models.GenericIPAddressField(protocol='IPv4', help_text='h')
    indent = models.CharField(max_length=1, default='-', help_text='l')
    user = models.CharField(max_length=5, default='-', help_text='u, frank')
    time = models.DateTimeField(help_text='t')
    method = models.CharField(max_length=6, default='-', help_text='%r -> m')
    url = models.CharField(max_length=500, default='-', help_text='%r -> U')
    protocol = models.CharField(max_length=15, default='-', help_text='%r -> H')
    status = models.CharField(max_length=15, help_text='>s')
    size = models.CharField(max_length=15, help_text='b')
    referrer = models.URLField(help_text='Referer')
    agent = models.CharField(max_length=600, help_text='User-agent')
    other = models.CharField(max_length=10, help_text='User-agent')

    def __str__(self):
        return f'{self.ip} | {self.status}'
