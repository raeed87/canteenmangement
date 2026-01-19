from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FoodItem, Order, OrderItem
from django.db import transaction, connection
from django.core.management import execute_from_command_line

def home_view(request):
    return render(request, 'home.html')

def menu_view(request):
    # Ensure database is ready
    ensure_database_ready()
    food_items = FoodItem.objects.all()
    return render(request, 'menu.html', {'food_items': food_items})

def ensure_database_ready():
    """Ensure database tables exist and have data"""
    try:
        # Check if tables exist
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders_fooditem';")
            if not cursor.fetchone():
                # Tables don't exist, create them
                from django.core.management import call_command
                call_command('migrate', verbosity=0, interactive=False)
                
        # Check if we have data
        if not FoodItem.objects.exists():
            create_sample_data()
            
    except Exception as e:
        print(f"Database setup error: {e}")
        # Try to create tables anyway
        try:
            from django.core.management import call_command
            call_command('migrate', verbosity=0, interactive=False)
            create_sample_data()
        except:
            pass

def create_sample_data():
    """Create sample food items and admin user"""
    try:
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
        from django.contrib.auth.models import User
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            
    except Exception as e:
        print(f"Sample data creation error: {e}")

def setup_database():
    """Setup database with initial data if needed"""
    try:
        # Run migrations first
        from django.core.management import execute_from_command_line
        import sys
        
        # Temporarily redirect stdout to suppress migration output
        old_stdout = sys.stdout
        sys.stdout = open('/dev/null', 'w') if hasattr(sys, 'stdout') else sys.stdout
        
        try:
            execute_from_command_line(['manage.py', 'migrate', '--run-syncdb'])
        except:
            pass
        finally:
            if sys.stdout != old_stdout:
                sys.stdout.close()
            sys.stdout = old_stdout
        
        with transaction.atomic():
            # Check if we have food items
            if not FoodItem.objects.exists():
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
                    FoodItem.objects.create(name=item['name'], price=item['price'])
                    
            # Create admin user if needed
            from django.contrib.auth.models import User
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
                
    except Exception as e:
        print(f"Database setup error: {e}")

def place_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '').strip()
        payment_method = request.POST.get('payment_method', 'upi')
        
        if not customer_name:
            messages.error(request, 'Customer name is required')
            return redirect('menu')
        
        order = Order.objects.create(
            customer_name=customer_name,
            payment_method=payment_method if payment_method in ['upi', 'card'] else 'upi'
        )
        total = 0
        has_items = False
        
        for food_item in FoodItem.objects.all():
            quantity = int(request.POST.get(f'quantity_{food_item.id}', 0))
            if quantity > 0:
                OrderItem.objects.create(
                    order=order,
                    food_item=food_item,
                    quantity=quantity
                )
                total += food_item.price * quantity
                has_items = True
        
        if not has_items:
            order.delete()
            messages.error(request, 'Please select at least one item')
            return redirect('menu')
        
        order.total_amount = total
        order.save()
        
        return render(request, 'payment.html', {'order': order})
    
    return redirect('menu')

def process_payment(request, order_id):
    if request.method == 'POST':
        try:
            order = Order.objects.get(id=order_id)
            action = request.POST.get('action')
            
            if action == 'confirm':
                order.payment_status = 'paid'
                order.save()
                return render(request, 'bill.html', {'order': order})
            elif action == 'cancel':
                order.payment_status = 'failed'
                order.save()
                messages.error(request, 'Payment cancelled')
                return redirect('menu')
        except Order.DoesNotExist:
            messages.error(request, 'Order not found')
    
    return redirect('menu')