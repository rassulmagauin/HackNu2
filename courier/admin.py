from django.contrib import admin
from .models import Courier

@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'order')

