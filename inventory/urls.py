from django.urls import path
from .views import index, display_laptops, display_desktops, display_mobiles, add_lap, add_desk, add_mob

urlpatterns = [
    path('', index, name='index'), 
    path('laptops', display_laptops, name='laptops'), 
    path('desktops', display_desktops, name='desktops'), 
    path('mobiles', display_mobiles, name='mobiles'), 
    path('add_lap', add_lap, name='add_lap'), 
    path('add_mob', add_mob, name='add_mob'), 
    path('add_desk', add_desk, name='add_desk'), 
]

