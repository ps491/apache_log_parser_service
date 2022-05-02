import logging
from pathlib import Path

from celery import shared_task

from .models import LogFile, Log
from .services.parse_log_files import parse_log_files
from .services.re_log import re_logs_to_dict
from .services.read_chunks import read_rows_in_chunks
from django.conf import settings
from src.celery import app
log = logging.getLogger(__name__)


@app.task
def process_read_log_file_task(instance_id: int):
    """Запуск чтения файла"""
    log.info(__doc__)
    log.info('RUN TASK!!!!')
    log_file = LogFile.objects.get(pk=instance_id)
    path = Path(log_file.file)
    with open(path, 'r') as f:
        # делим на чанки по 1000 строк
        # TODO: также желательно предварительно делить сам файл на чанки для чтения - дополнительный цикл for
        for piece in read_rows_in_chunks(f, settings.LOG_CHUNK):
            log_data = []
            for row in piece:  # прогоняем строки чанка через регулярки, сохраняем в виде списка словарей
                log_data.append(re_logs_to_dict(row))

            Log.objects.bulk_create([Log(**i) for i in log_data])
            log.info('CREATED Log objects by chunk!!!!')
    log_file.processed = True
    log_file.save()


@shared_task
def process_parse_logs_task():
    """Запуск парсинга и сохранения логов в бд"""
    parse_log_files()

