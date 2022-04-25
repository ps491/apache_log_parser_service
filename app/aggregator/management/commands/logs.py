import logging

from django.core.management.base import BaseCommand

from aggregator.services.parse_log_files import parse_log_files

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Parse log files'

    def handle(self, *args, **kwargs):
        # parse_log_files()
        return "Complete!!"
