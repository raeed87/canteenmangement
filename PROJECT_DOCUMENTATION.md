# 🍽️ CANTEEN ORDER & BILLING SYSTEM
## (Using Django – Python)

### 1. Introduction

The Canteen Order & Billing System is a web-based application developed using the Django framework of Python. The purpose of this project is to digitize the manual canteen ordering process by providing a simple, fast, and efficient way to take customer orders and generate bills automatically.

In traditional canteens, billing is usually done manually, which can cause calculation errors, delays, and crowding. This system solves those problems by allowing customers to select food items from a web interface and instantly receive the total bill.

### 2. Problem Statement

Most small canteens still use manual order taking and billing, which leads to:
- Time-consuming order processing
- Human calculation errors
- Long queues during peak hours
- Difficulty in maintaining sales records

There is a need for a simple, low-cost, and easy-to-use web-based system to automate the ordering and billing process.

### 3. Objectives of the Project

The main objectives of this project are:
- To display the canteen food menu online
- To allow customers to place orders easily
- To calculate the total bill automatically
- To generate a simple receipt
- To reduce manual work and errors

### 4. Scope of the Project

This project is designed for:
- College canteens
- School canteens
- Small food stalls
- Cafeterias

The system focuses only on ordering and billing, making it simple and suitable for beginners. Advanced features like online payment and login can be added later.

### 5. Proposed System

The proposed system is a Django-based web application that automates the ordering and billing process.

**Working of the System:**
1. Food items and prices are stored in the database
2. The menu is displayed on a web page
3. The customer selects quantities for items
4. The system calculates the total cost automatically
5. A receipt page displays the final bill

### 6. Advantages of the Proposed System

- Easy to use and understand
- Reduces billing errors
- Saves time for customers and staff
- Improves efficiency of canteen operations
- Can be accessed from any device with a browser

### 7. Technology Used

- **Frontend:** HTML, CSS
- **Backend:** Python (Django Framework)
- **Database:** SQLite
- **Server:** Django Development Server

### 8. System Architecture

The system follows Django's MVT (Model–View–Template) architecture:
- **Model:** Stores menu items and prices in the database
- **View:** Handles business logic and bill calculation
- **Template:** Displays menu and receipt to users

This separation makes the system clean, organized, and easy to maintain.

### 9. Modules of the System

#### 1. Menu Module
- Displays food items and prices
- Data fetched from the database

#### 2. Order Module
- Takes quantity input from the user
- Processes customer orders

#### 3. Billing Module
- Calculates total cost automatically
- Generates final bill

#### 4. Receipt Module
- Displays the total amount
- Confirms successful order

### 10. Database Design

#### Models Used:

**FoodItem Model:**
- name: CharField (food item name)
- price: DecimalField (item price)

**Order Model:**
- customer_name: CharField (customer name)
- created_at: DateTimeField (order timestamp)
- total_amount: DecimalField (total bill amount)

**OrderItem Model:**
- order: ForeignKey to Order
- food_item: ForeignKey to FoodItem
- quantity: PositiveIntegerField

### 11. Implementation Details

#### Key Files Structure:
```
canteen management/
├── manage.py
├── requirements.txt
├── canteen/
│   ├── settings.py
│   ├── urls.py
│   └── templates/
│       ├── menu.html
│       └── bill.html
└── orders/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── admin.py
```

#### Core Functionality:
- **Menu Display:** Shows all available food items with prices
- **Order Processing:** Captures customer name and item quantities
- **Bill Generation:** Automatically calculates total and displays receipt
- **Admin Panel:** Allows staff to manage food items and view orders

### 12. Testing and Results

The system has been tested with:
- Multiple food items and quantities
- Various customer orders
- Bill calculation accuracy
- Admin panel functionality

**Test Results:**
- ✅ Menu displays correctly
- ✅ Orders process successfully
- ✅ Bills calculate accurately
- ✅ Admin panel works properly

### 13. Limitations of the System

- No user login system
- No online payment integration
- No order history storage for customers
- Basic user interface
- No inventory management

These limitations can be addressed in future enhancements.

### 14. Future Enhancements

- Token-based ordering system
- Online payment gateway
- Daily sales report
- Enhanced admin dashboard
- Inventory management system
- Customer order history
- Mobile-responsive design
- Print receipt functionality

### 15. Installation and Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Database Setup:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create Admin User:**
   ```bash
   python create_admin.py
   ```

4. **Add Sample Data:**
   ```bash
   python populate_data.py
   ```

5. **Run Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access Application:**
   - Main Menu: http://127.0.0.1:8000
   - Admin Panel: http://127.0.0.1:8000/admin

### 16. Conclusion

The Canteen Order & Billing System using Django is a simple and effective solution for automating the canteen ordering process. It reduces manual effort, minimizes errors, and improves service speed. The project is ideal for beginners and serves as a strong foundation for learning web development using Python and Django.

The system successfully demonstrates the practical application of Django's MVT architecture and provides a real-world solution to common canteen management problems. With its clean code structure and extensible design, it can be easily enhanced with additional features as needed.

---

**Project Developed By:** [Your Name]  
**Technology:** Django (Python)  
**Database:** SQLite  
**Year:** 2024