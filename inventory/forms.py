from django.forms import ModelForm
from .models import *

class MobileForm(forms.ModelForm):
    
    class Meta:
        model = Mobile
        fields = "__all__"

class DesktopForm(forms.ModelForm):
    
    class Meta:
        model = Desktop
        fields = "__all__"

class LaptopForm(forms.ModelForm):
    
    class Meta:
        model = Laptop
        fields = "__all__"

