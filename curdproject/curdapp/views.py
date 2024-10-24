from django.shortcuts import render, redirect
from .models import Item

# Create item
def create_item(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        Item.objects.create(name=name, description=description)
        return redirect('list_items')
    return render(request, 'curdapp/create_item.html')

# Read items (list view)
def list_items(request):
    items = Item.objects.all()
    return render(request, 'curdapp/list_items.html', {'items': items})

# Update item
def update_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.save()
        return redirect('list_items')
    return render(request, 'curdapp/update_item.html', {'item': item})

# Delete item
def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('list_items')
