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