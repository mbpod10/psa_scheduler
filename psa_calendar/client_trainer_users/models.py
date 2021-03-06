from django.db import models

# Create your models here.


class Workout(models.Model):
    workout_name = models.CharField(max_length=256, blank=False, null=False)
    repititions = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.workout_name
