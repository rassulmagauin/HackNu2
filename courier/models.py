from django.db import models
# Create your models here.

class Courier(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    
    company_name = models.CharField(max_length=50, blank = True)
    def __str__(self):
        return self.name
