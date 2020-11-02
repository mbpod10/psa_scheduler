from django.contrib import admin
from django.urls import path, include
from .views import event_list, client_list

urlpatterns = [
    path('events/', event_list),
    path('clients/', client_list),
]
