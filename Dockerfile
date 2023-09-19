# pull official base image
FROM python:3.11.2-slim

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt update
RUN apt --force-yes -y install postgresql libpq-dev postgresql-contrib python3-dev
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv
RUN pipenv install psycopg2-binary
RUN pipenv install Pillow
RUN pipenv install crispy-bootstrap5 && pipenv install django-crispy-forms
RUN pipenv install --system

# Copy project
COPY . /code/
