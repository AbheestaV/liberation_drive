from django.shortcuts import render, redirect
from ...models import MenuItem
from ...forms import MenuItemForm

def menu_add_item(request, restaurant_id):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant_id = restaurant_id
            menu_item.save()
            return redirect('menu_items_for_restaurant', restaurant_id=restaurant_id)
    else:
        form = MenuItemForm()

    return render(request, 'menu_add_item.html', {'form': form})
