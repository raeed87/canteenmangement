import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteen.settings')
django.setup()

from django.contrib.auth.models import User

# Create admin user
try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Admin user created successfully!")
        print("Username: admin")
        print("Password: admin123")
    else:
        print("Admin user already exists!")
except Exception as e:
    print(f"Error creating admin user: {e}")