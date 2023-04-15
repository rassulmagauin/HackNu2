from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import Courier
from .serializers import CourierSerializer

import os
# Create your views here.

class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

@csrf_exempt
def send_sms(request):
    
    if request.method == 'POST':
        number = request.POST['phone']
        token = os.environ.get('TOKEN')
        text = os.environ.get('TEXT')

        url = 'http://hakaton-sms.gov4c.kz/api/smsgateway/send'
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)}
        data = {'phone': '{}', 'smsText': '{}'.format(number, text)}

        response = requests.post(url, headers=headers, json=data)
        response.accepted_renderer = 'json' # set the accepted renderer manually
        response.accepted_media_type = 'application/json'
        return HttpResponse({response.status_code}, status=status.HTTP_201_CREATED)
    return HttpResponse({'Invalid data provided'}, status.HTTP_400_BAD_REQUEST)
    

def get_price(request):
    return 5

