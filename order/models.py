from django.db import models
# Create your models here.
from courier.models import Courier

class Order(models.Model):
    request_id = models.CharField(max_length=255)
    IIN = models.CharField(max_length=12)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    aIIN = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name='orders', null=True)
    date = models.DateTimeField(blank=False, null=False, auto_now=True)
    region = models.CharField(max_length=50, default='Kazakhstan')
    city = models.CharField(max_length=50, default='Astana')
    street = models.CharField(max_length=50, default='Kabanbay Batyr')
    building_number = models.CharField(max_length=50, blank=True)
    apartment = models.CharField(max_length=50, blank=True)
    entry = models.CharField(max_length=50, blank=True)
    floor = models.CharField(max_length=50, blank=True)
    corpus = models.CharField(max_length=50, blank=True)
    jk = models.CharField(max_length=50, blank=True)
    additional = models.TextField(blank=True)