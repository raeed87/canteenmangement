#!/bin/bash

echo "Starting Canteen Management System..."

# Run migrations on startup
echo "Running database migrations..."
python manage.py migrate --noinput

# Create admin user if it doesn't exist
echo "Setting up admin user..."
python create_admin.py

# Populate sample data
echo "Adding sample food items..."
python populate_data.py

# Start the application
echo "Starting Gunicorn server..."
exec gunicorn canteen.wsgi:application