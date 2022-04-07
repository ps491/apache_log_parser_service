## Условия
Задание 2.
Используя django/flask(на выбор), реализовать приложение, которое является агрегатором данных из access логов apache с сохранением в БД.
Разбор файлов должен выполняться по cron'у .

В приложении реализовать такие функции:
- авторизация (пользователи в БД)
- просмотр данных сохраненных в БД (группировка по IP, по дате, выборка по промежутку дат)
- API для получения данных в виде JSON (смысл тот же: получение данных по временному промежутку, возможность группировать/фильтровать по IP)
- конфигурация через файл настроек (где лежат логи, маска файлов, и все, что Вам потребуется для настройки приложения)

СУБД: mysql/postgresql

# Запуск
1. запуск
```sh
$ docker-compose -f docker-compose.dev.yml up --build
```
2. закидываем дефолтные данные, включая админа 
```sh
$ docker exec -it app poetry run python manage.py loaddata default_data.json
```
3. админка логин - admin, пароль - 25658545
`http://127.0.0.1:8000/api/swagger/` - документация API

`http://127.0.0.1:8000/admin/` - админка

# Пояснения
1. Перед запуском необходимо настроить/изменить путь LOG_PATH в файле .env - указать директорию откуда будут браться 
файлы логов для агрегатора по крону. В локальной разработке путь до файлов может быть любой, в development, 
т.е. через docker из контейнера путь до файлов только через директорию logs к которой примонтирована директория из 
переменных окружения LOG_PATH в docker-compose
2. Если нет переменной LOG_PATH, то выставляется дефолтный путь - директория logs внутри проекта
и ожидается что файлы будут там появляться.
3. Периодичность проверки и обработки логов установлена по дефолту - в 1 час
(для тестов 15 сек- надо раскомментировать в конфиге ofelia).
4. Начал реализовывать функционал на сelery + celery-beat, но как выяснилось django-celery-beat отвалилась 
и не ставится на Django выше 4 версии. Можно было бы откатить версии и продолжить, но было принято решение 
создать новый велосипед :-))). 
Периодичность выполняется по кастомной команде, запускает ее шедулер [Ofelia](https://github.com/mcuadros/ofelia). 
Дальнейшая обработка файлов передается в задачи Dramatiq


# Database dump/load
```shell
$ docker exec -it app sh -c "poetry run python manage.py dumpdata --natural-foreign --natural-primary --exclude=contenttypes --exclude=auth.Permission --exclude=admin.logentry --exclude=sessions.session --indent 4 > default_data.json"
docker exec -it app poetry run python manage.py loaddata default_data.json
```
## Enter to container
```sh
$ docker exec -it <id container or name> bash
$ docker exec -it <id container or name> poetry run <command>
```
