#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "=== Starting Django Build Process ==="

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Make start script executable
echo "🔧 Making start script executable..."
chmod +x start.sh

# Collect static files
echo "📂 Collecting static files..."
python manage.py collectstatic --noinput --verbosity=2

echo "✅ Build completed successfully!"