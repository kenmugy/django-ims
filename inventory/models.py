from django.db import models

# Create your models here.
class Device(models.Model):
    type = models.CharField('type',max_length = 100)
    price = models.IntegerField(default= 0)
    choices = (
        (
            'AVAILABLE', 'Item ready to be sold'
        ),
        (
            'SOLD', 'Item sold'
        ),
        (
            'RESTOCING', 'Iten restocking in a few days'
        ),
    )
    status = models.CharField(max_length = 100, choices = choices, default='SOLD')
    issues = models.CharField(max_length = 100, default='No Issues')

    class Meta:
        abstract = True

    def __str__(self):
        return f'Type: {type} | Price: {price}'
        
class Laptop(Device):
    pass

    
class Desktop(Device):
    pass

class Mobile(Device):
    pass


        