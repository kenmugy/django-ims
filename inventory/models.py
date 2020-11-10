from django.db import models

# Create your models here.
class Device(models.Model):
    type = models.CharField('type',max_length = 100)
    price = models.IntegerField(default= 0)
    status = models.CharField(max_length = 100, default='SOLD')
    issues = models.CharField(max_length = 100, default='No Issues')

    def __str__(self):
        return f'Type: {type} | Price: {price}'
        
class Laptop(Device):
    pass

    
class Desktop(Device):
    pass

class Mobile(Device):
    pass


        