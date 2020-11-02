from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from datetime import timedelta, datetime
import logging

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Trainer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    hours_clocked = models.PositiveIntegerField(blank=True, null=True)
    wages = models.FloatField(blank=True, null=True)

    def clean(self):
        if self.hours_clocked:
            money = ((self.hours_clocked / 60) * 10)
            print(money)
            self.wages = money
            self.save()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True)
    trainer = models.ForeignKey(Trainer, null=True, on_delete=models.SET_NULL)
    day = models.DateField(u'Day Of The Event', help_text=u'Day Of The Event')
    start_time = models.TimeField(u'Starting Time', help_text=u'Starting Time')
    end_time = models.TimeField(
        u'Final Time', help_text='Final Time', null=True, blank=True)
    notes = models.TextField(
        u'Textual Notes', help_text='Textual Notes', blank=True, null=True)
    # time = models.CharField(max_length=256, null=True, blank=True)
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
                print(self.end_time, self.start_time)
                time1 = datetime.strptime(str(self.end_time), '%H:%M:%S')
                time2 = datetime.strptime(
                    str(self.start_time), '%H:%M:%S')
                difference = time1-time2
                print(difference)
                # self.time = difference
                total = 0
                print(str(difference).split(":"))
                acc = str(difference).split(":")
                total = total + int(acc[0]) * 60
                total = total + int(acc[1])
                print(total)
                self.time = total
                self.trainer.hours_clocked = total + self.trainer.hours_clocked
                money = ((total / 60) * 10) + self.trainer.wages
                self.trainer.wages = money
                self.trainer.save()

    def __str__(self):
        if self.end_time:
            # time = int(str(self.end_time)) - int(str(self.start_time))
            return str(self.client.last_name) + " " + str(self.day) + " (" + str(self.start_time) + ") " + str(self.trainer.last_name) + " CLOSED "
        else:
            return str(self.client.last_name) + " " + str(self.day) + " (" + str(self.start_time) + ") " + str(self.trainer.last_name) + " OPEN"
