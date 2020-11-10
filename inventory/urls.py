from django.urls import path
from .views import index, display_laptops

urlpatterns = [
    path('', index, name='index'), 
    path('laptops', display_laptops, name='laptops'), 
]

