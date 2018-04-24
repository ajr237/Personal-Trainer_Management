from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^1/$', views.calendar, name='calendar_url'),
    url(r'^g/$', views.calendar_by_period, name='calendar_by'),
    ]
