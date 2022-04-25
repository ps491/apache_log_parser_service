from ..components import BASE_DIR, config

print('LOCAL SETTINGS!!!!')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ['*']

# в локалке путь до файлов может быть любой...
LOG_PATH = config('LOG_PATH', default=BASE_DIR / 'logs')
