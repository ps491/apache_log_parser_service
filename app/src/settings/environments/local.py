from src.settings.components import BASE_DIR, config

print('LOCAL SETTINGS!!!!')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ['*']

LOG_PATH = config('LOG_PATH')  # в локалке путь до файлов может быть любой...
