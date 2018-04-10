from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from . models import Client

@login_required
def dashboard(request):

    user = get_user_model()

    context = {
        'user': user,
    }

    return render(request, 'clients/dashboard.html', context)

def client_list_view(request):

    client_list = Client.objects.filter(user=request.user)

    context = {
        'client_list': client_list,
    }

    return render(request, 'clients/client_list.html', context)
