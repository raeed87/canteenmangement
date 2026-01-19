# Canteen Order & Billing System

A minimal Django-based web application for canteen order management and billing.

## Setup Instructions

1. Install Django:
   ```
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create admin user (optional):
   ```
   python manage.py createsuperuser
   ```

4. Start the server:
   ```
   python manage.py runserver
   ```

5. Visit http://127.0.0.1:8000 to access the canteen menu

## Features

- View food menu with prices
- Place orders by selecting quantities
- Automatic bill calculation
- Order history in admin panel
- Add/edit food items via admin panel

## Admin Panel

Access http://127.0.0.1:8000/admin to manage food items and view orders.

## Usage

1. Enter customer name
2. Select quantities for desired food items
3. Click "Place Order" to generate bill
4. View itemized bill with total amount