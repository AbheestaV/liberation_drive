from django.db import models

# Create your models here.

class User(models.Model):
    USER_TYPES = [
        ('customer', 'Customer'),
        ('restaurant', 'Restaurant'),
        ('delivery_agent', 'Delivery Agent'),
        ('driver', 'Driver'),
    ]
    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=255)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.user_type})"
    

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links to the User table
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_STATUS = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('preparing', 'Preparing'),
        ('en_route', 'En Route'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    ORDER_TYPE = [
        ('food', 'Food'),
        ('ride', 'Ride'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True)
    delivery_agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='delivery_agent_orders')
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    placed_at = models.DateTimeField(auto_now_add=True)
    delivery_address = models.CharField(max_length=255)
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE, default='food')

    def __str__(self):
        return f"Order {self.id} - {self.customer.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} (Order {self.order.id})"

class Trip(models.Model):
    TRIP_STATUS = [
        ('assigned', 'Assigned'),
        ('picked_up', 'Picked Up'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agent_trips')
    pickup_address = models.CharField(max_length=255, null=True, blank=True)
    dropoff_address = models.CharField(max_length=255, null=True, blank=True)
    pickup_time = models.DateTimeField(null=True, blank=True)
    dropoff_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=TRIP_STATUS, default='assigned')

    def __str__(self):
        return f"Trip for Order {self.order.id} - {self.status}"

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('apple_pay', 'Apple Pay'),
    ]

    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    payment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.payment_status}"

class Vehicle(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=20)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"

class Ride(models.Model):
    RIDE_STATUS = [
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_rides')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver_rides')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    pickup_address = models.CharField(max_length=255)
    dropoff_address = models.CharField(max_length=255)
    ride_status = models.CharField(max_length=20, choices=RIDE_STATUS, default='requested')
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    ride_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride {self.id} - {self.ride_status}"

class RideReview(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_reviews')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver_reviews')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    review = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for Ride {self.ride.id} - Rating: {self.rating}"

class RidePayment(models.Model):
    PAYMENT_METHODS = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('apple_pay', 'Apple Pay'),
    ]

    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    ride = models.OneToOneField(Ride, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_ride_payments')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver_ride_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    payment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Ride {self.ride.id} - {self.payment_status}"

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class OrderCoupon(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('order', 'coupon')
