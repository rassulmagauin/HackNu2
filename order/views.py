from django.shortcuts import render

from rest_framework import viewsets
from .models import Order, Address
from .serializers import OrderSerializer, AddressSerializer
from courier.models import Courier
from courier.serializers import CourierSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('date')
    serializer_class = OrderSerializer


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()