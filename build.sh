#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser if it doesn't exist
python create_admin.py

# Populate sample data
python populate_data.py

echo "Build completed successfully!"