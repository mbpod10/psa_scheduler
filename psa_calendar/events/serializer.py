from rest_framework import serializers
from .models import Client, Trainer, Event


class ClientSerializier(serializers.ModelSerializer):
    # event = serializers.RelatedField(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    # event = serializers.RelatedField(read_only=True)

    class Meta:
        model = Trainer
        fields = '__all__'


class EventPostSerializer(serializers.ModelSerializer):
    # trainer = serializers.RelatedField(read_only=True)
    # client = serializers.RelatedField(read_only=True)

    class Meta:
        model = Event
        # depth = 1
        fields = '__all__'
        # fields = ('id', 'trainer', 'client', 'day',
        #           'start_time', 'end_time', 'time')


class EventSerializer(serializers.ModelSerializer):
    # trainer = serializers.RelatedField(read_only=True)
    # client = serializers.RelatedField(read_only=True)

    class Meta:
        model = Event
        depth = 1
        fields = '__all__'
        # fields = ('id', 'trainer', 'client', 'day',
        #           'start_time', 'end_time', 'time')
