from django.shortcuts import render
from .serializer import EventSerializer, ClientSerializier, EventPostSerializer
from .models import Event, Client, Trainer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def event_list(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(http_method_names=['POST', 'PUT'])
@csrf_exempt
def event_post(request):
    if request.method == 'POST' or request.method == 'PUT':
        json = JSONParser().parse(request)
        serializer = EventPostSerializer(data=json)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        print(JsonResponse(serializer.data))
        return JsonResponse(serializer.errors)


def client_list(request):
    clients = Client.objects.all()
    serializer = ClientSerializier(clients, many=True)
    return JsonResponse(serializer.data, safe=False)
