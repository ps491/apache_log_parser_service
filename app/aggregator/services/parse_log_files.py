import logging
from pathlib import Path

from src.settings.components.base import LOG_PATH
from ..models import LogFile
from ..tasks import process_read_log_file_task

log = logging.getLogger(__name__)


def parse_log_files():
    """Parse log files"""
    # Периодическая проверка директории на наличие новых файлов
    log.info(__doc__)
    path = Path(LOG_PATH)
    for f in path.iterdir():
        # Если файла нет в бд, то вносим его с processed=False.
        # Далее его "подхватит" task после обработки выставит значение True
        # Если создание из админки, то его подхватит сигнал и отправит в таск
        if f.suffix == '.log':  # TODO: вынести логику проверки расширения в отдельный файл
            obj, created = LogFile.objects.get_or_create(file=f)
            if created:
                log.info(f'Создание записи в бд LogFile\n{obj.id}\n\n')
                process_read_log_file_task.send(obj.id)  # отправляем файл(id записи) в таски на обработку
                # process_read_log_file_task(obj.id)

        else:
            log.info(f'мусор {f.name} {f.suffix}\n\n')
        # TODO: при смене директории и/или переносе файлов логов, они будут считаться НОВЫМИ:
        #  - либо удалять файлы после парсинга
        #  - либо прогонять повторно и удалять дубли записей в бд, рискованно (будут те которые не факт что дубли...)
        #  - переименовывать файлы на выходе и отсеивать в цикле проверок - распарсивать названия файлов
        #  (вводить правила наименования приходящих файлов)

