from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import FoodItem, Order, OrderItem

# Custom admin site
class CanteenAdminSite(AdminSite):
    site_header = 'Canteen Administrator'
    site_title = 'Canteen Admin'
    index_title = 'Welcome to Canteen Administration'

admin_site = CanteenAdminSite(name='canteen_admin')

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'formatted_price']
    
    def formatted_price(self, obj):
        return f"₹{obj.price}"
    formatted_price.short_description = 'Price'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'formatted_total', 'payment_method', 'payment_status', 'created_at']
    list_filter = ['payment_method', 'payment_status', 'created_at']
    readonly_fields = ['created_at']
    
    def formatted_total(self, obj):
        return f"₹{obj.total_amount}"
    formatted_total.short_description = 'Total Amount'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'food_item', 'quantity', 'formatted_subtotal']
    
    def formatted_subtotal(self, obj):
        return f"₹{obj.subtotal}"
    formatted_subtotal.short_description = 'Subtotal'

# Register models with custom admin site
admin_site.register(FoodItem, FoodItemAdmin)
admin_site.register(Order, OrderAdmin)
admin_site.register(OrderItem, OrderItemAdmin)