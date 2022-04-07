from decouple import Csv

from src.settings.components import config, BASE_DIR
from src.settings.components.base import (
    INSTALLED_APPS,
    MIDDLEWARE
)
print('DEVELOPMENT SETTINGS!!!!')
DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default=config('DOMAIN'))

# из контейнера путь до файлов только через директорию logs к которой примонтирована директория из переменных окружения
# 'LOG_PATH' в docker-compose
LOG_PATH = BASE_DIR / 'logs'

INSTALLED_APPS += (
    # # Better debug:
    # 'debug_toolbar',
    #
    #
    # # Linting migrations:
    # 'django_migration_linter',
    #
    # # django-test-migrations:
    # 'django_test_migrations.contrib.django_checks.AutoNames',
    # # This check might be useful in production as well,
    # # so it might be a good idea to move `django-test-migrations`
    # # to prod dependencies and use this check in the main `settings.py`.
    # # This will check that your database is configured properly,
    # # when you run `python manage.py check` before deploy.
    # 'django_test_migrations.contrib.django_checks.DatabaseConfiguration',
    #
    # # django-extra-checks:
    # 'extra_checks',
)

# MIDDLEWARE += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
#
#     # https://github.com/bradmontgomery/django-querycount
#     # Prints how many queries were executed, useful for the APIs.
#     'querycount.middleware.QueryCountMiddleware',
# )

def _custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return DEBUG and request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK':
        'server.settings.environments.development._custom_show_toolbar',
}
