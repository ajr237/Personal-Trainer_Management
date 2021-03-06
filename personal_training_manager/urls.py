"""personal_training_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from clients import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.dashboard, name='dashboard_url'),
    url(r'^clients/', include('clients.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^tests/', include('health_fitness_tests.urls')),
    # url(r'^calendar/', include('schedule.urls')),
    # url(r'^calendar1/', include('planner.urls')),
]
