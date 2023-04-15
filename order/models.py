from django.db import models
# Create your models here.
from courier.models import Courier

class Address(models.Model):
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building_number = models.CharField(max_length=50, blank=True)
    apartment = models.CharField(max_length=50, blank=True)
    entry = models.CharField(max_length=50, blank=True)
    floor = models.CharField(max_length=50, blank=True)
    corpus = models.CharField(max_length=50, blank=True)
    jk = models.CharField(max_length=50, blank=True)
    additional = models.TextField(blank=True)

class Order(models.Model):
    request_id = models.CharField(max_length=255)
    IIN = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    aIIN = models.IntegerField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name='orders', null=True)
    date = models.DateField(blank=False, null=False, default='2022-12-12')