from django import forms
from ..models import Restaurant
from ..models import MenuItem
from ..models import Order
from ..models import Ride
from ..models import Payment


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'phone_number']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'available', 'image_url']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_address']

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['pickup_address', 'dropoff_address', 'fare']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_method']