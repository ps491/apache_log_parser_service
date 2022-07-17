## Apache log parser
An application that is an aggregator of data from apache access logs
with saving in the database. File parsing is done by cron.

The application has the following functions:
- authorization (users in the database)
- viewing data stored in the database (grouping by IP, by date, selection by date interval)
- API for receiving data in the form of JSON (the meaning is the same: obtaining data by time interval, the ability
group/filter by IP)
- configuration through the settings file (where the logs, file mask, and everything you need to configure the application are)
DBMS: mysql/postgresql

# run
0. add LOG_PATH to .env.dev
1. launch
```sh
$ docker-compose -f docker-compose.dev.yml up --build
```

2. upload default data, including admin
```sh
$ docker exec -it app poetry run python manage.py loaddata default_data.json
```
3. admin login - admin, password - 25658545
`http://127.0.0.1:8000/api/swagger/` - API documentation

`http://127.0.0.1:8000/admin/` - admin panel

# Explanations
1. Before starting, you need to configure / change the LOG_PATH path in the .env file - specify the directory from where they will be taken
log files for the cron aggregator (using the pwd command, you can determine the path and paste it). In local development, the path to the files can be any, in development,
those. through docker from the container, the path to the files only through the logs directory to which the directory from
LOG_PATH environment variables in docker-compose
2. If there is no LOG_PATH variable, then the default path is set - the logs directory inside the project
and it is expected that the files will appear there.
3. The frequency of checking and processing logs is set by default - at 1 hour
(for tests, 15 seconds - you need to uncomment it in the ofelia config).
4. I started to implement functionality on celery + celery-beat, but as it turned out, django-celery-beat fell off
and is not installed on Django above version 4. It would be possible to roll back the versions and continue, but the decision was made
create a new bike :-))).
Periodicity is performed by a custom command, its scheduler [Ofelia] (https://github.com/mcuadros/ofelia) launches it.
Further file processing is transferred to Dramatiq tasks


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
