#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "Starting build process..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Make migrations
echo "Creating migrations..."
python manage.py makemigrations

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist
echo "Creating admin user..."
python create_admin.py

# Populate sample data
echo "Populating sample data..."
python populate_data.py

echo "Build completed successfully!"