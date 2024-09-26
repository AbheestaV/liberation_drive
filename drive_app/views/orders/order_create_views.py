from django.shortcuts import render, redirect
from ...models import Order, OrderItem
from ...forms import OrderForm

def order_create(request, restaurant_id):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.restaurant_id = restaurant_id
            order.save()
            return redirect('orders_list')
    else:
        form = OrderForm()

    return render(request, 'order_create.html', {'form': form})