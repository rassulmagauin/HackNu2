from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('request_id','cost', 'status', 'phone' ,'date', 'region', 'city')
    list_filter = ['request_id', 'date', 'status']

