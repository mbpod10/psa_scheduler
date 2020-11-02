from django.shortcuts import render
from .serializer import EventSerializer, ClientSerializier
from .models import Event, Client, Trainer
from django.http import JsonResponse

# Create your views here.


def event_list(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)


def client_list(request):
    clients = Client.objects.all()
    serializer = ClientSerializier(clients, many=True)
    return JsonResponse(serializer.data, safe=False)
