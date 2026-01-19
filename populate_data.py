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
try:
    FoodItem.objects.all().delete()
    print("Cleared existing food items")
except:
    print("No existing food items to clear")

for item in food_items:
    try:
        FoodItem.objects.create(name=item['name'], price=item['price'])
        print(f"Created: {item['name']} - Rs.{item['price']}")
    except Exception as e:
        print(f"Error creating {item['name']}: {e}")

print("Sample food items setup completed!")