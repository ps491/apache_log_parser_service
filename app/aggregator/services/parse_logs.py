from pathlib import Path

from .path_log_files import logs_path
from ..models import LogFile


def parse_log_files():

    path = Path(logs_path())
    db_files = LogFile.objects.all()
    for f in path.iterdir():
        # Если файла нет в бд, то вносим его с processed=False.
        # Далее его "подхватит" post_save сигнал и после обработки выставит значение True
        # if f.suffix == '.log' and not db_files.filter(file=f).exists():
        #     LogFile.objects.create(file=f)
        if f.suffix == '.log':
            LogFile.objects.get_or_create(file=f)
            print(f.name, f.suffix)
        else:
            print('мусор', f.name, f.suffix)
        # TODO: при смене директории и переносе файлов логов, они будут считаться НОВЫМИ:
        #  - либо удалять файлы после парсинга
        #  - либо прогонять повторно и удалять дубли записей в бд (не факт что дубли...)
        #  - переименовывать файлы и отсеивать в цикле - распарсивать названия файлов (вводить правила
        #  наименования приходящих файлов)
    print('парсим файлы')
