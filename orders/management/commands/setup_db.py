from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from orders.models import FoodItem

class Command(BaseCommand):
    help = 'Setup database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Setting up database...')
        
        # Create admin user
        try:
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
                self.stdout.write('Admin user created: admin/admin123')
            else:
                self.stdout.write('Admin user already exists')
        except Exception as e:
            self.stdout.write(f'Error creating admin: {e}')
        
        # Create food items
        food_items = [
            {'name': 'Veg Burger', 'price': 45.00},
            {'name': 'Masala Dosa', 'price': 35.00},
            {'name': 'Paneer Sandwich', 'price': 40.00},
            {'name': 'Chai', 'price': 15.00},
            {'name': 'Cold Drink', 'price': 20.00},
            {'name': 'Samosa', 'price': 12.00},
            {'name': 'Pav Bhaji', 'price': 50.00},
        ]
        
        try:
            FoodItem.objects.all().delete()
            for item in food_items:
                FoodItem.objects.create(name=item['name'], price=item['price'])
                self.stdout.write(f"Created: {item['name']} - ₹{item['price']}")
            self.stdout.write('Sample food items created successfully!')
        except Exception as e:
            self.stdout.write(f'Error creating food items: {e}')
        
        self.stdout.write('Database setup completed!')