from django.contrib import admin
from .models import Laptop, Desktop, Mobile

# Register your models here.
admin.site.register(Laptop)
admin.site.register(Desktop)
admin.site.register(Mobile)
