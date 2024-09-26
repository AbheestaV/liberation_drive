from django.shortcuts import render
from ...models import Restaurant

def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})