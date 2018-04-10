from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Client(models.Model):

    GENDER_CHOICES = (
        ('1', 'Male'),
        ('0', 'Female')
    )

    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(blank=True)
    contact_number = models.IntegerField(blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()

    @property
    def age(self):
        import datetime
        return int((datetime.date.today() - self.date_of_birth).days / 365.25  )

    @property
    def gender_description(self):
        if self.gender == '1':
            return 'male'
        else:
            return 'female'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
