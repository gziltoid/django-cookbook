#! /bin/bash

set -e

python manage.py makemigrations cookbook
python manage.py migrate
python manage.py loaddata unit
python manage.py runserver 0.0.0.0:8000
