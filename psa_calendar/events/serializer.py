from rest_framework import serializers
from .models import Client, Trainer, Event


class ClientSerializier(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    # trainer = TrainerSerializer()

    class Meta:
        model = Event
        depth = 1
        fields = '__all__'
        # fields = ('trainer.last_name', 'start_time')
