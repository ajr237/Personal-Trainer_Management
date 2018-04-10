from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'clients'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard_url'),
    url(r'^client_list/$', views.client_list_view, name='client_list_url'),
]
