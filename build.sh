#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "=== Starting Django Build Process ==="

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Create database directory
echo "🗄️ Creating database directory..."
mkdir -p /tmp

# Run migrations
echo "🗄️ Running migrations..."
python manage.py migrate --verbosity=2

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