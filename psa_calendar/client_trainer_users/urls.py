from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, WorkoutViewSet, workout_list, user_login

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('workouts', WorkoutViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("workout_list/", workout_list),
    path("user_login/", user_login),
]
