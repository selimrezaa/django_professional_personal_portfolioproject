from django.contrib import admin
from django.urls import path
from .views import *
app_name = 'app_main'

urlpatterns = [
        path('', index, name='index'),
        path('service-details/<pk>/', service_details, name='service_details',)
]
