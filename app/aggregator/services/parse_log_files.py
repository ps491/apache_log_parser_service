from pathlib import Path

from .path_log_files import logs_path
from ..models import LogFile
from ..tasks import process_parse_log_task


def parse_log_files():
    """Parse log files"""
    path = Path(logs_path())
    for f in path.iterdir():
        # Если файла нет в бд, то вносим его с processed=False.
        # Далее его "подхватит" task после обработки выставит значение True
        # Если создание из админки, то его подхватит сигнал и отправит в таск
        if f.suffix == '.log':  # TODO: вынести логику проверки расширения в отдельный файл
            obj, created = LogFile.objects.get_or_create(file=f)
            if created:
                print(f'Создание записи LogFile\n{obj.file}\n\n')
                # process_parse_log_task.send(instance.id)
                process_parse_log_task(obj.id)

        else:
            print('мусор', f.name, f.suffix)
        # TODO: при смене директории и/или переносе файлов логов, они будут считаться НОВЫМИ:
        #  - либо удалять файлы после парсинга
        #  - либо прогонять повторно и удалять дубли записей в бд, рискованно (будут те которые не факт что дубли...)
        #  - переименовывать файлы и отсеивать в цикле - распарсивать названия файлов (вводить правила
        #  наименования приходящих файлов)
    print('парсим файлы')
