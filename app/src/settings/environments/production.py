from ..components import config

DEBUG = False

ALLOWED_HOSTS = [
    config('DOMAIN'),
    # We need this value for `healthcheck` to work:
    'localhost',
]
