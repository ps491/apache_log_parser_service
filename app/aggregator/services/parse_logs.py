from pathlib import Path

from ..models import LogFile, TestLog


def parse_logs(instance_id: int):
    log_file = LogFile.objects.get(pk=instance_id)
    path = Path(log_file.file)
    # TODO: https: // gist.github.com / sumeetpareek / 9644255
    with open(path, 'r') as f:
        for row in f.read().splitlines():
            print(row)
            TestLog.objects.create(row=row)

    log_file.processed = True
    log_file.save()
