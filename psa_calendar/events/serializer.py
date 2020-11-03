from rest_framework import serializers
from .models import Client, Trainer, Event
from datetime import timedelta, datetime
import logging


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


class EventSerializer(serializers.ModelSerializer):
    # trainer = serializers.RelatedField(read_only=True)
    # client = serializers.RelatedField(read_only=True)

    class Meta:
        model = Event
        depth = 1
        fields = '__all__'
        # fields = ('id', 'trainer', 'client', 'day',
        #           'start_time', 'end_time', 'time')


class EventPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):

        start_time = validated_data['start_time']
        end_time = validated_data['end_time']
        time1 = datetime.strptime(str(end_time), '%H:%M:%S')
        time2 = datetime.strptime(str(start_time), '%H:%M:%S')

        difference = time1-time2

        print(difference)
        total = 0
        print(str(difference).split(":"))
        acc = str(difference).split(":")
        total = total + int(acc[0]) * 60
        total = total + int(acc[1])
        print(total)
        validated_data['time'] = total

        print(validated_data['trainer'].wages)
        trainer = validated_data['trainer']

        print(trainer.wages)

        if trainer.minutes_clocked:
            trainer.minutes_clocked = total + trainer.minutes_clocked
            money = ((total / 60) * 10) + trainer.wages
            trainer.wages = money
            print(trainer.wages)
            trainer.save()

        else:
            trainer.minutes_clocked = total
            money = ((total / 60) * 10)
            trainer.wages = money
            print(trainer.wages)
            trainer.save()

        # print(start_time, end_time)

        return Event.objects.create(**validated_data)
