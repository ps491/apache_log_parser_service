from src.settings.components import config

REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT",)
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
print('CELERY_BROKER_URL', CELERY_BROKER_URL)
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
# CELERY_BEAT_SCHEDULE = {
#     'save-google-events-to-db': {
#         'task': 'clinic.tasks.sync_google_events_db',
#         'schedule': crontab(minute='*/2'),
#     }
# }
