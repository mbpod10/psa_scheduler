from django.contrib import admin
from django.urls import path, include
from .views import event_list, client_list, event_post, event_detail

urlpatterns = [
    path('events/', event_list),
    path('clients/', client_list),
    path('events/post/', event_post),
    path('events/<int:pk>/', event_detail),
]
