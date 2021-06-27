#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn ToDoList_Django.wsgi:application --workers 3 --bind 0.0.0.0:8000
