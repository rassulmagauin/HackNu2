from rest_framework import serializers

from .models import Order
from courier.models import Courier

import json,requests, os
class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'
    
class OrderSerializer(serializers.ModelSerializer):
    courier = CourierSerializer(many=False)

    class Meta:
        model = Order
        fields = '__all__'

    def _get_or_create_courier(self, courier, order):
        courier_obj, created = Courier.objects.get_or_create(
            **courier
        )
        order.courier = courier_obj

    def create(self, validated_data):
        courier = validated_data.pop('courier', [])
        order = Order.objects.create(**validated_data)
        self._get_or_create_courier(courier, order)
        return order
    
    def update(self, instance, validated_data):
        courier = validated_data.pop('courier', None)
        if courier is not None: 
            instance.courier = None
            self._get_or_create_courier(courier, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance