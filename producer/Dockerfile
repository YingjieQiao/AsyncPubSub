FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .
RUN pip install -r requirements.txt
