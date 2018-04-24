from django.db import models

from clients.models import Client
from django.utils import timezone

# Create your models here.
class Session(models.Model):
    client = models.ForeignKey(Client)
    duration = models.DurationField()
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=80)

    def __str__(self):
        return f"{ self.client.get_full_name } Session"
