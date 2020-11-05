from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, WorkoutViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('workouts', WorkoutViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
