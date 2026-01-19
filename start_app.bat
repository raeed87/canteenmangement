@echo off
echo ========================================
echo   CANTEEN ORDER & BILLING SYSTEM
echo ========================================
echo.
echo Checking system status...
python test_system.py
echo.
echo ========================================
echo Starting Django development server...
echo.
echo 🏠 Home Page: http://127.0.0.1:8000
echo 🍽️ Menu Page: http://127.0.0.1:8000/menu
echo ⚙️ Admin Panel: http://127.0.0.1:8000/admin
echo    Username: admin
echo    Password: admin123
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.
python manage.py runserver