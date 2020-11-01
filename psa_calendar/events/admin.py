from django.contrib import admin
from .models import Event, Client, Trainer
# Register your models here.

admin.site.register(Event)
admin.site.register(Client)
admin.site.register(Trainer)
