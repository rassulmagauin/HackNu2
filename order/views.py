from django.shortcuts import render

from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework import status
import os
import requests
import math
from django.http import HttpResponse

def search(*params):
    address = ''
    for param in params:
        if param:
            address += param + ' '
    
    url = "https://address-from-to-latitude-longitude.p.rapidapi.com/geolocationapi"
    headers =  {
	    "X-RapidAPI-Key": "4b6fc0a3camsh3650402cb52ad17p18c16ajsn00f3e37ee952",
	    "X-RapidAPI-Host": "address-from-to-latitude-longitude.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params={"address": address})
    return response["Results"][0].latitude, response["Results"][0].longitude
    # return response

def def_cost():
    initial_address = os.environ.get("ADDRESS")
    print(initial_address)
    return search(initial_address)

def get_cost(*params):
    initial_address = os.environ.get("ADDRESS")
    lat1, lng1 = search(*params)
    lat2, lng2 = search(initial_address)
    lat, lng = lat2 - lat1, lng2 - lng1

    return 'cost is: ' + math.sqrt(lat*lat + lng*lng)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('date')
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # cost = get_cost(serializer.validated_data['region'], serializer.validated_data['city'])
            cost = def_cost()
            return HttpResponse({cost}, status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status.HTTP_400_BAD_REQUEST)
