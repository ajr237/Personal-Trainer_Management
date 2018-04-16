from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'clients'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard_url'),
    url(r'^client_list/$', views.client_list_view, name='client_list_url'),
    url(r'^add_client/$', views.create_client_view, name='create_client_url'),
    url(r'^client_list/client_information/(?P<pk>\d+)/$', views.client_information_view, name='client_information_url'),
    url(r'^client_list/client_information/delete/(?P<pk>\d+)/$', views.client_delete_view, name='client_delete_url')
]
