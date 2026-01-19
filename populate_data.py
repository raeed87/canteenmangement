import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteen.settings')
django.setup()

from orders.models import FoodItem

# Create sample food items with Indian prices
food_items = [
    {'name': 'Veg Burger', 'price': 45.00},
    {'name': 'Masala Dosa', 'price': 35.00},
    {'name': 'Paneer Sandwich', 'price': 40.00},
    {'name': 'Chai', 'price': 15.00},
    {'name': 'Cold Drink', 'price': 20.00},
    {'name': 'Samosa', 'price': 12.00},
    {'name': 'Pav Bhaji', 'price': 50.00},
]

# Clear existing items and add new ones
FoodItem.objects.all().delete()

for item in food_items:
    FoodItem.objects.create(name=item['name'], price=item['price'])

print("Indian food items created with Rupee pricing!")