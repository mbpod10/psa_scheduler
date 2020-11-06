from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer, WorkoutSerializer
from .models import Workout
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

    def create(self, request, args, **kwargs):

        # print(request.data)
        data = JSONParser().parse(request)
        serializer = WorkoutSerializer(data=data)
        # print(request)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@csrf_exempt
def workout_list(request):
    if request.method == 'GET':
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WorkoutSerializer(data=data)

        errors = []

        if data['repititions'] < 5:
            errors.append("Repititions Must Be More Than 5")

        if len(data['workout_name']) < 7:
            errors.append("Workout Name Must Be More Than 5")

        if errors:
            return JsonResponse({"errors": errors}, status=200)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)
        # return JsonResponse({"errors": errors}, status=400)


@api_view(['POST', 'GET'])
@csrf_exempt
def user_login(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        contains_upper = False

        for x in range(0, len(data['password'])):
            if data['password'][x].isupper():
                contains_upper = True

        if len(data['password']) < 6:
            # errors.append({"error": 'Password Must Be More Than 6 Characters'})
            return JsonResponse({"error": "Password Must Be More Than 6 Characters"})

        if data['password'].isalpha():
            # errors.append({"error": "Password Must Contain Numbers"})
            return JsonResponse({"error": "Password Must Contain Numbers"})

        if not contains_upper:
            # errors.append(
            # {"error": 'Password Must Contain One Capital Letter'})
            return JsonResponse({"error": "Password Must Contain One Capital Letter"})

        # print(errors)
        # if errors:
        #     return JsonResponse({"errors": errors}, status=200)

        if serializer.is_valid():
            # serializer.save()
            user = User.objects.create_user(**data)
            Token.objects.create(user=user)
            return JsonResponse(serializer.data, status=201)
        # return user

        # user = User.objects.create_user(**data)
        # Token.objects.create(user=user)
        # return user
