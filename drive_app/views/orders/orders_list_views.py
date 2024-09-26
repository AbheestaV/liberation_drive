from django.shortcuts import render
from ...models import Order

def orders_list(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'orders_list.html', {'orders': orders})