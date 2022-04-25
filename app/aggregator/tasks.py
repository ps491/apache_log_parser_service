import logging
from pathlib import Path

import dramatiq
from .models import LogFile, Log
from .services.re_log import re_logs_to_dict
from .services.read_chunks import read_rows_in_chunks
from django.conf import settings

log = logging.getLogger(__name__)


@dramatiq.actor
def process_read_log_file_task(instance_id: int):
    """Запуск чтения файла"""
    log.info(__doc__)
    print('RUN TASK!!!!')
    log_file = LogFile.objects.get(pk=instance_id)
    path = Path(log_file.file)
    with open(path, 'r') as file:
        # делим на чанки по 1000 строк

        for piece in read_rows_in_chunks(file, settings.LOG_CHUNK):
            log_data = []
            # прогоняем строки чанка через регулярки, сохраняем в виде списка словарей
            for row in piece:
                log_data.append(re_logs_to_dict(row))

            Log.objects.bulk_create([Log(**i) for i in log_data])
            print("CREATED Log objects by chunk")
    log_file.processed = True
    log_file.save()


# @dramatiq.actor
# def process_parse_logs_task(data: List[dict]):
#     """Запуск парсинга и сохранения логов в бд"""
#     result = Log.objects.bulk_create([Log(**i) for i in data])
#     print(result)
