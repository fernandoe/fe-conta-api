#!/bin/sh

export DATABASE_URL=mysql://root:password@mysql:3306/fe-conta

python manage.py runserver 0.0.0.0:8000
