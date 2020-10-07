FROM python:3.9.0

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/app

WORKDIR /usr/app

COPY ./pyproject.toml /usr/app
COPY ./poetry.lock /usr/app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

ADD . /usr/app
