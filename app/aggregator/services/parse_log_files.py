import logging
from pathlib import Path

from django.conf import settings

from ..models import LogFile
from ..tasks import process_read_log_file_task

log = logging.getLogger(__name__)


def parse_log_files():
    """Parse log files"""
    # Periodically check the directory for new files
    log.info(__doc__)
    path = Path(settings.LOG_PATH)
    for f in path.iterdir():
        # If the file is not in the database, then we add it with processed=False.
        # Next, it will be "picked up" by task after processing, it will set the value to True
        # If the creation is from the admin panel, then it will be picked up by a signal and sent to the task
        if f.suffix == '.log':  # TODO: move the extension check logic to a separate file
            obj, created = LogFile.objects.get_or_create(file=f)
            if created:
                log.info(f'Creating an entry in the LogFile database\n{obj.id}\n\n')
                process_read_log_file_task.send(obj.id)  # send the file (record id) to tasks for processing
                # process_read_log_file_task(obj.id)

        else:
            log.info(f'мусор {f.name} {f.suffix}\n\n')
        # TODO: when changing directory and/or moving log files, they will be considered NEW:
        # - either delete files after parsing
        # - either run it again and delete duplicate records in the database, it's risky (there will be those that are not the fact that they are duplicates ...)
        # - rename files on output and filter out in the check loop - parse filenames
        # (enter rules for naming incoming files)
