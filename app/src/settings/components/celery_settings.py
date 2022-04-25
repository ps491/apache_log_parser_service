from celery.schedules import crontab

from src.settings.components import config

REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT",)
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
print('CELERY_BROKER_URL', CELERY_BROKER_URL)
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_BEAT_SCHEDULE = {
    'periodic_parse_logs': {
        'task': 'aggregator.tasks.process_parse_logs_task',
        'schedule': crontab(minute='*/2'),
    }
}
