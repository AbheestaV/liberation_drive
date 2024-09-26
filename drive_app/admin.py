from django.contrib import admin
from .models import User, Restaurant, MenuItem, Order, OrderItem, Trip, Payment, Vehicle, Ride, RideReview, RidePayment, Coupon, OrderCoupon

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Trip)
admin.site.register(Payment)
admin.site.register(Vehicle)
admin.site.register(Ride)
admin.site.register(RideReview)
admin.site.register(RidePayment)
admin.site.register(Coupon)
admin.site.register(OrderCoupon)
