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

def update_func(request, dform, redir):
    form = dform()
    if request.method == 'POST':
        form = dform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redir)

    return render(request, 'inventory/update.html', {'form': form})
    
def add_lap(request):
    return update_func(request, LaptopForm, 'laptops')

def add_desk(request):
    return update_func(request, DesktopForm, 'desktops')

def add_mob(request):
    return update_func(request, MobileForm, 'mobile')
    