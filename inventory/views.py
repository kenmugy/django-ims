from django.shortcuts import render
from .models import Laptop, Desktop, Mobile

# Create your views here.
def index(request):
    return render(request, 'inventory/index.html', {})

def display_laptops(request):
    context = {
        'laptops': Laptop.objects.all(),
        'title': 'laptops'
    }
    return render(request, 'inventory/index.html', context)

def display_desktops(request):
    context = {
        'desktops': Laptop.objects.all(),
        'title': 'desktops'
    }
    return render(request, 'inventory/index.html', context)

def display_mobiles(request):
    context = {
        'mobiles': Laptop.objects.all(),
        'title': 'mobiles'
    }
    return render(request, 'inventory/index.html', context)

