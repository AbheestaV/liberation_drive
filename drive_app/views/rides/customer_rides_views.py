from django.shortcuts import render
from ...models import Ride

def customer_rides(request):
    rides = Ride.objects.filter(customer=request.user)
    return render(request, 'customer_rides.html', {'rides': rides})