from django.shortcuts import render

from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework import status
import os
import requests
import math
from django.http import HttpResponse
import json

def search(*params):
    address = ' '.join(str(param) for param in params)
    
    url = "https://address-from-to-latitude-longitude.p.rapidapi.com/geolocationapi"
    headers =  {
	    "X-RapidAPI-Key": "4b6fc0a3camsh3650402cb52ad17p18c16ajsn00f3e37ee952",
	    "X-RapidAPI-Host": "address-from-to-latitude-longitude.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params={"address": address})
    # return response(["Results"][0], response["Results"][0])
    # return response
    data = json.loads(response.content)
    return [data["Results"][0]["latitude"], data["Results"][0]["longitude"]]

def get_cost(*params):
    initial_address = os.environ.get("ADDRESS")
    lat1, lng1 = search(params)
    lat2, lng2 = search(initial_address)
    lat, lng = lat2 - lat1, lng2 - lng1

    return 'cost is: ' + str(int(math.sqrt(lat*lat + lng*lng) * 15 + 250))

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('date')
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cost = get_cost(serializer.validated_data['region'], serializer.validated_data['city'], serializer.validated_data['street'])
            return HttpResponse(cost, status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    