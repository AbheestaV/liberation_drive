from django.shortcuts import render
from ...models import MenuItem

def menu_items_list(request, restaurant_id):
    menu_items = MenuItem.objects.filter(restaurant_id=restaurant_id)
    return render(request, 'menu_items_list.html', {'menu_items': menu_items})