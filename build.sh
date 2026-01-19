#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "=== Installing System Dependencies ==="
# Install PostgreSQL development libraries
apt-get update
apt-get install -y libpq-dev

echo "=== Starting Django Build Process ==="

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Setup database
echo "🗄️ Setting up database..."
python setup_db.py

# Collect static files
echo "📂 Collecting static files..."
python manage.py collectstatic --noinput --verbosity=2

# Create superuser
echo "👤 Creating admin user..."
python create_admin.py

# Populate sample data
echo "🍽️ Adding sample food items..."
python populate_data.py

echo "✅ Build completed successfully!"