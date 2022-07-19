#!/usr/bin/env bash
set -e

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
gunicorn svfoundation.wsgi:application --bind 0.0.0.0:8000
