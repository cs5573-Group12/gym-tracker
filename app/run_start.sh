#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn -b :8080 --timeout 600 --chdir /app app.wsgi:application
