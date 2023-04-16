from django.contrib import admin
from .models import Order
# from courier.models import Courier

# class OrderCourierInline(admin.TabularInline):
#     model = Courier
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('request_id','cost', 'status', 'phone' ,'date', 'region', 'city')
    list_filter = ['request_id', 'date', 'status']
    # inlines = [OrderCourierInline]
