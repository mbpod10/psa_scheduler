from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .models import Workout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # @csrf_exempt
    # def create(self, validated_data):

    #     contains_upper = False
    #     errors = []

    #     for x in range(0, len(validated_data['password'])):
    #         if validated_data['password'][x].isupper():
    #             contains_upper = True

    #     if len(validated_data['password']) < 6:
    #         errors.append('Password Must Be More Than 6 Characters')

    #     if validated_data['password'].isalpha():
    #         errors.append('Password Must Contain Numbers')

    #     if not contains_upper:
    #         errors.append('Password Must Contain One Capital Letter')

    #     if errors:
    #         raise serializers.ValidationError(
    #             {'errors': errors}, code=400)
    #         # return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

    #     user = User.objects.create_user(**validated_data)
    #     Token.objects.create(user=user)
    #     return user


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'workout_name', 'repititions']
