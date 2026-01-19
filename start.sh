#!/bin/bash

echo "Starting Canteen Management System..."

# Run migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Setup database with initial data
echo "Setting up initial data..."
python manage.py setup_db

# Start the application
echo "Starting Gunicorn server..."
exec gunicorn canteen.wsgi:application