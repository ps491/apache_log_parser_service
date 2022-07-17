from django.db.models.signals import post_save
from django.dispatch import receiver

from aggregator.models import LogFile
from aggregator.tasks import process_read_log_file_task


@receiver(post_save, sender=LogFile)
def item_signal(sender, instance: LogFile, created, **kwargs):
    """Creating a file entry is done in order to be able to also
     add or remove logs manually from the admin panel"""
    # disable signal, when create model from command "manage.py loaddata",
    # because will be errors
    if kwargs.get('raw', False):
        return False

    if created:
        # process_parse_log_task.send(instance.id)
        process_read_log_file_task(instance.id)
    return True
