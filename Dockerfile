FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_PIPFILE /Pipfile

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN python -m pip install --upgrade pip && pip install pipenv && pipenv install --system

COPY . /code/