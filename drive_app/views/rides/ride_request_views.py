from django.shortcuts import render, redirect
from ...models import Ride
from ...forms import RideForm

def ride_request(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.customer = request.user
            ride.ride_status = 'requested'
            ride.save()
            return redirect('customer_rides')
    else:
        form = RideForm()

    return render(request, 'request_ride.html', {'form': form})