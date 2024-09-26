from django.shortcuts import render, redirect
from ...models import Payment
from ...forms import PaymentForm  # Create a form for payment

def process_order_payment(request, order_id):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.customer = request.user
            payment.order_id = order_id
            payment.payment_status = 'completed'
            payment.save()
            return redirect('orders_list')
    else:
        form = PaymentForm()

    return render(request, 'process_payment.html', {'form': form})


def process_ride_payment(request, ride_id):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.customer = request.user
            payment.ride_id = ride_id
            payment.payment_status = 'completed'
            payment.save()
            return redirect('customer_rides')
    else:
        form = PaymentForm()

    return render(request, 'process_payment.html', {'form': form})
