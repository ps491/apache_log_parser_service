# pull official base image
FROM python:3.8

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
#RUN apk update \
#    && apk add postgresql-dev gcc libressl-dev libffi-dev python3-dev musl-dev zlib-dev jpeg-dev cargo libmagic

# install dependencies
COPY ./pyproject.toml ./poetry.lock ./app/entrypoint.sh /
#COPY ./pyproject.toml ./poetry.lock /
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
