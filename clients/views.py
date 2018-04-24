from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils import timezone

from . models import Client
from . forms import ClientForm

from planner.models import Session

@login_required
def dashboard(request):

    user = request.user
    clients = Client.objects.filter(user=user)
    sessions = Session.objects.filter(client__user=user)

    context = {
        'user': user,
        'clients': clients,
        'sessions': sessions,
    }

    return render(request, 'clients/dashboard.html', context)

def client_list_view(request):

    client_list = Client.objects.filter(user=request.user)

    context = {
        'client_list': client_list,
    }

    return render(request, 'clients/client_list.html', context)

def create_client_view(request):

    if request.method == 'POST':
        client_form = ClientForm(request.POST)

        if client_form.is_valid():
            client = client_form.save(commit=False)
            client.user = request.user
            client.save()
            return redirect('clients:client_list_url')

    form = ClientForm()

    context = {
        'form': form,
    }
    return render(request, 'clients/add_client.html', context)

def client_information_view(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            return redirect('clients:client_information_url', pk=pk)
    else:
        form = ClientForm(instance=client)
    clients = Client.objects.order_by('-date_added')
    counter = 0
    k = []
    for i in clients:
        if i != client and counter <3:
            k.append(i)
            counter += 1

    return render(request, 'clients/client_information.html', {'form': form, 'client': client, 'k': k})

def client_delete_view(request, pk):
    client = Client.objects.filter(pk=pk)
    client.delete()
    return redirect('clients:client_list_url')
