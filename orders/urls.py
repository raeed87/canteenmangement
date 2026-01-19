from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('order/', views.place_order, name='place_order'),
    path('payment/<int:order_id>/', views.process_payment, name='process_payment'),
]