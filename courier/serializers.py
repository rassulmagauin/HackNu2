from rest_framework import serializers

from .models import Courier
from order.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CourierSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=False, required=True)

    class Meta:
        model = Courier
        fields = '__all__'