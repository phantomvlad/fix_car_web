# pull official base image
FROM python:3.11.2-slim

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system && apt update && apt --force-yes -y install postgresql libpq-dev postgresql-contrib python3-dev

# Copy project
COPY . /code/
