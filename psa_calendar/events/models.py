from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from datetime import timedelta, datetime
import logging
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    client_name = models.CharField(max_length=256)

    def __str__(self):
        return self.client_name


class Trainer(models.Model):
    trainer_name = models.CharField(max_length=256)
    minutes_clocked = models.PositiveIntegerField(blank=True, null=True)
    wages = models.FloatField(default=0.00)

    def clean(self):
        if self.minutes_clocked:
            money = ((self.minutes_clocked / 60) * 10)
            print(money)
            self.wages = money
            self.save()

    def __str__(self):
        return self.trainer_name


class Event(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, blank=True, null=True, related_name='client')
    trainer = models.ForeignKey(
        Trainer, null=True, on_delete=models.SET_NULL, related_name='trainer')
    day = models.DateField(u'Day Of The Event', help_text=u'Day Of The Event')
    start_time = models.TimeField(u'Starting Time', help_text=u'Starting Time')
    end_time = models.TimeField(
        u'Final Time', help_text='Final Time', blank=True, null=True)
    notes = models.TextField(
        u'Textual Notes', help_text='Textual Notes', blank=True, null=True)
    time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        print(type(new_start), type(new_end),
              type(fixed_end), type(fixed_start))
        print("Helllllllllll")

    def clean(self):
        if self.end_time:
            if self.end_time <= self.start_time:
                raise ValidationError(
                    'Ending times must be after starting times')
            events = Event.objects.filter(day=self.day)
            if events.exists():
                for event in events:
                    if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                        BaseException('There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))
        self.check_time()

    def check_time(self):
        if self.end_time:
            if self.time:
                pass
            else:
                time1 = datetime.strptime(str(self.end_time), '%H:%M:%S')
                time2 = datetime.strptime(str(self.start_time), '%H:%M:%S')
                difference = time1-time2
                total = 0
                acc = str(difference).split(":")
                total = total + int(acc[0]) * 60
                total = total + int(acc[1])
                self.time = total
                if self.trainer.minutes_clocked:
                    self.trainer.minutes_clocked = total + self.trainer.minutes_clocked
                    money = ((total / 60) * 10) + self.trainer.wages
                    self.trainer.wages = money
                    self.trainer.save()
                else:
                    self.trainer.minutes_clocked = total
                    money = ((total / 60) * 10)
                    self.trainer.wages = money
                    self.trainer.save()

    def __str__(self):
        if self.end_time:
            return str(self.client.client_name).split(" ")[1] + " " + str(self.day) + " (" + str(self.start_time) + ") " + str(self.trainer.trainer_name).split(" ")[1] + " CLOSED "
        else:
            return str(self.client.client_name).split(" ")[1] + " " + str(self.day) + " (" + str(self.start_time) + ") " + str(self.trainer.trainer_name).split(" ")[1] + " OPEN"
