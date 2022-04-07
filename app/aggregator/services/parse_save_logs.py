import logging
from typing import List

from aggregator.models import Log

log = logging.getLogger(__name__)


def save_logs(data: List[dict], ):
    result = Log.objects.bulk_create([Log(**i) for i in data])
    print(result)
