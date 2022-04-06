from src.settings.components import config

DEBUG = False

ALLOWED_HOSTS = [
    # TODO: check production hosts
    config('DOMAIN'),

    # We need this value for `healthcheck` to work:
    'localhost',
]


