from django.urls import path
from .views import index, display_laptops, display_desktops, display_mobiles

urlpatterns = [
    path('', index, name='index'), 
    path('laptops', display_laptops, name='laptops'), 
    path('desktops', display_desktops, name='desktops'), 
    path('mobiles', display_mobiles, name='mobiles'), 
]

