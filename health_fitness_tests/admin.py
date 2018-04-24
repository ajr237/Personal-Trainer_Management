from django.contrib import admin

# Register your models here.
from .models import BodyHeight, BodyMass

admin.site.register(BodyHeight)
admin.site.register(BodyMass)
