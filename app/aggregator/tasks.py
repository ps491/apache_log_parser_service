from typing import List

import dramatiq
import logging

from aggregator.services.parse_save_logs import save_logs
from aggregator.services.read_log_file import read_log_file

log = logging.getLogger(__name__)


@dramatiq.actor
def process_read_log_file_task(instance_id: int):
    """Запуск чтения файла"""
    log.info(__doc__)
    read_log_file(instance_id)
    # TODO: проверяем есть ли файл


@dramatiq.actor
def process_parse_logs_task(data: List[dict]):
    """Запуск парсинга и сохранения логов в бд"""
    log.info(__doc__)
    save_logs(data)
