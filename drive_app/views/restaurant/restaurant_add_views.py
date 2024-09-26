from django.shortcuts import render, redirect
from ...models import Restaurant
from ...forms import RestaurantForm

def restaurant_add(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    
    return render(request, 'restaurant_add.html', {'form': form})
    