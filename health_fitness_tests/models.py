from django.db import models
from django.utils import timezone

from clients.models import Client

# Create your models here.
class BodyHeight(models.Model):
    client = models.ForeignKey(Client)
    height = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name} Height"

class BodyMass(models.Model):
    client = models.ForeignKey(Client)
    mass = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name} Mass"
