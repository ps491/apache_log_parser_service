import dramatiq
import logging

log = logging.getLogger(__name__)


@dramatiq.actor
def process_parse_logs():
    print("Проверка файлов")
    # получаем директорию из конфига
    # проверяем файлы, сверяем с записями в бд
    # если не распарсен, от отправляем в таск на парсинг


