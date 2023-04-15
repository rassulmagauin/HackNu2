from rest_framework import serializers

from .models import Order, Address
from courier.models import Courier

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        exclude = ['order']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False, required=False)
    courier = CourierSerializer(many=False)

    class Meta:
        model = Order
        fields = '__all__'
