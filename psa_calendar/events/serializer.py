from rest_framework import serializers
from .models import Client, Trainer, Event
from datetime import timedelta, datetime
import logging


class ClientSerializier(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        depth = 1
        fields = '__all__'


class EventPostSerializer(serializers.ModelSerializer):

    # global_start_time = datetime.time("0:0:0", '%H:%M:%S')
    global_start_time = datetime.now

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):

        if validated_data['end_time']:
            start_time = validated_data['start_time']
            self.global_start_time = start_time
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
        print(self.global_start_time)
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.trainer = validated_data.get('trainer', instance.trainer)
        instance.start_time = validated_data.get(
            'start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)

        if instance.start_time and instance.end_time:
            print(validated_data['start_time'], instance.start_time)
            print("not doing anyting")
            print(self.global_start_time)
            return instance

        if instance.end_time:
            print(instance.end_time)
            time1 = datetime.strptime(str(instance.end_time), '%H:%M:%S')
            time2 = datetime.strptime(str(instance.start_time), '%H:%M:%S')
            difference = time1-time2
            print(difference)
            total = 0
            print(str(difference).split(":"))
            acc = str(difference).split(":")
            total = total + int(acc[0]) * 60
            total = total + int(acc[1])
            print(total)
            instance.time = total
            print(instance.time)

            print(instance.trainer.wages)

            if instance.trainer.minutes_clocked:
                instance.trainer.minutes_clocked = total + instance.trainer.minutes_clocked
                money = ((total / 60) * 10) + instance.trainer.wages
                instance.trainer.wages = money
                print(instance.trainer.wages)
                instance.trainer.save()
                instance.save()

            else:
                instance.trainer.minutes_clocked = total
                money = ((total / 60) * 10)
                instance.trainer.wages = money
                print(instance.trainer.wages)
                instance.trainer.save()
                instance.save()
        print(self.global_start_time)
        return instance
