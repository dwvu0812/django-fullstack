#!/bin/bash

# Run database migrations
poetry run python manage.py migrate

# Create superuser if it doesn't exist
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com  
export DJANGO_SUPERUSER_PASSWORD=admin
poetry run python manage.py createsuperuser --noinput || true

# Start the Django development server
poetry run python manage.py runserver 0.0.0.0:8000
