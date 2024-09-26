from django.urls import path

from .views.restaurant import restaurant_add_views, restaurant_detail_views, restaurant_list_views
from .views.orders import order_create_views, orders_list_views
from .views.menu import menu_add_item_views, menu_items_list_views
from .views.payments import payment_views
from .views.rides import ride_request_views, customer_rides_views
from .views.auth import auth_views

urlpatterns = [
    # Restaurant views
    path('restaurants/', restaurant_list_views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:pk>/', restaurant_detail_views.restaurant_detail, name='restaurant_detail'),
    path('restaurants/add', restaurant_add_views.restaurant_add, name='restaurant_add'),

    # Menu item views
    path('restaurants/<int:restaurant_id>/menu/', menu_items_list_views.menu_items_list, name='menu_items_list'),
    path('restaurants/<int:restaurant_id>/menu/add/', menu_add_item_views.menu_add_item, name='menu_add_item'),

    # Order views
    path('orders/', orders_list_views.orders_list, name='order_list'),
    path('restaurants/<int:restaurant_id>/order/', order_create_views.order_create, name='order_create'),

    # Ride views
    path('rides/', customer_rides_views.customer_rides, name='customer_rides'),
    path('rides/request', ride_request_views.ride_request, name='request_ride'),

    # Payment views
    path('order/<int:order_id>/payment/', payment_views.process_order_payment, name='process_order_payment'),
    path('ride/<int:ride_id>/payment/', payment_views.process_ride_payment, name='process_ride_payment'),

    # Auth views
    path('register/', auth_views.register, name='register'),
    path('login/', auth_views.login, name='login'),
]   