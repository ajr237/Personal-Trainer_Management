from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'health_fitness_tests'

urlpatterns = [
    url(r'^$', views.test_client_list, name='health_client_list_url'),
    url(r'^client_dashboard/(?P<pk>\d+)/$', views.client_dashboard, name='client_dashboard_url'),
    url(r'^update_add/(?P<pk>\d+)/$', views.update_add, name='update_add_url'),
    # url(r'^client_list/$', views.client_list_view, name='client_list_url'),
]
