from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FoodItem, Order, OrderItem

def home_view(request):
    return render(request, 'home.html')

def menu_view(request):
    food_items = FoodItem.objects.all()
    return render(request, 'menu.html', {'food_items': food_items})

def place_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '').strip()
        payment_method = request.POST.get('payment_method', 'cash')
        
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