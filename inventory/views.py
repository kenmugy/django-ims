from django.shortcuts import render, redirect
from inventory.forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'inventory/index.html', {})

def display_laptops(request):
    context = {
        'items': Laptop.objects.all(),
        'title': 'laptops'
    }
    return render(request, 'inventory/index.html', context)

def display_desktops(request):
    context = {
        'items': Desktop.objects.all(),
        'title': 'desktops'
    }
    return render(request, 'inventory/index.html', context)

def display_mobiles(request):
    context = {
        'items': Mobile.objects.all(),
        'title': 'mobiles'
    }
    return render(request, 'inventory/index.html', context)

def add_lap(request):
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laptops')

    return render(request, 'inventory/update.html', {'form': form})
    