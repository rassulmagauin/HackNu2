from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('courier', views.CourierViewSet)

app_name= 'couriers'

urlpatterns = [
    path('', include(router.urls)),
    path('sendsms', views.send_sms, name='sendsms'),
    path('getprice', views.get_price, name='getprice')
]
