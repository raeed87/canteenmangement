from django.apps import AppConfig
from django.db import connection
from django.core.management.color import no_style

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    
    def ready(self):
        # Setup database when app starts
        self.setup_database()
    
    def setup_database(self):
        try:
            # Check if we need to create tables
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders_fooditem';")
                if not cursor.fetchone():
                    # Run migrations
                    from django.core.management import execute_from_command_line
                    execute_from_command_line(['manage.py', 'migrate', '--run-syncdb'])
                    
                    # Create initial data
                    self.create_initial_data()
        except Exception as e:
            print(f"Database setup error: {e}")
    
    def create_initial_data(self):
        try:
            from .models import FoodItem
            from django.contrib.auth.models import User
            
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
            
            for item in food_items:
                FoodItem.objects.get_or_create(
                    name=item['name'],
                    defaults={'price': item['price']}
                )
            
            # Create admin user
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
                
        except Exception as e:
            print(f"Initial data creation error: {e}")