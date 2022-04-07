import logging
from pathlib import Path
from typing import List

import dramatiq

from aggregator.models import LogFile, Log

from aggregator.services.re_log import re_logs_to_dict
from aggregator.services.read_chunks import read_rows_in_chunks

log = logging.getLogger(__name__)


@dramatiq.actor
def process_read_log_file_task(instance_id: int):
    """Запуск чтения файла"""
    log.info(__doc__)

    log_file = LogFile.objects.get(pk=instance_id)
    path = Path(log_file.file)
    with open(path, 'r') as f:
        # делим на чанки по 1000 строк
        # TODO: также желательно предварительно делить сам файл на чанки для чтения - дополнительный цикл for
        for piece in read_rows_in_chunks(f, 5):
            log_data = []
            for row in piece:  # прогоняем строки чанка через регулярки, сохраняем в виде списка словарей
                log_data.append(re_logs_to_dict(row))
            process_parse_logs_task.send(log_data)  # отправляем в таски
            # process_parse_logs_task(log_data)
    log_file.processed = True
    log_file.save()


@dramatiq.actor
def process_parse_logs_task(data: List[dict]):
    """Запуск парсинга и сохранения логов в бд"""
    result = Log.objects.bulk_create([Log(**i) for i in data])
    print(result)
