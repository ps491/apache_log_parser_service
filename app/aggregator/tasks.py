import dramatiq
import logging

from aggregator.services.parse_logs import parse_logs

log = logging.getLogger(__name__)


# @dramatiq.actor
def process_parse_log_task(instance_id: int):
    print("Запуск парсинга, чтение файла")
    parse_logs(instance_id)
    # TODO: проверяем есть ли файл


