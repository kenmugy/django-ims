from django.db import models

# Create your models here.
class Laptop(models.Model):
    Obj_type = models.CharField('type',max_length = 100)
    price = models.IntegerField(default= 0)
    status = models.CharField(max_length = 100, default='SOLD')
    issues = models.CharField(max_length = 100, default='No Issues')

    def __str__(self):
        return f'Type: {Obj_type} | Price: {price}'
        