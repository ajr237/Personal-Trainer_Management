from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'clients'

urlpatterns = [
    # url(r'^$', views.index2, name='index2'),
    url(r'^$', views.dashboard, name='dashboard_url'),
]
