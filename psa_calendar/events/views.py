from django.shortcuts import render
from .serializer import EventSerializer, ClientSerializier, EventPostSerializer
from .models import Event, Client, Trainer
from django.http import JsonResponse, HttpResponse
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


@api_view(http_method_names=['POST'])
@csrf_exempt
def event_post(request):
    if request.method == 'POST':
        json = JSONParser().parse(request)
        serializer = EventPostSerializer(data=json)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        print(JsonResponse(serializer.data))
        return JsonResponse(serializer.errors)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
@csrf_exempt
def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)

    except Event.DoesNotExist:
        return HttpResponse("Does not exist", status=404)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data, status=201)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventPostSerializer(event, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        event.delete()
        return HttpResponse(status=204)


def client_list(request):
    clients = Client.objects.all()
    serializer = ClientSerializier(clients, many=True)
    return JsonResponse(serializer.data, safe=False)
