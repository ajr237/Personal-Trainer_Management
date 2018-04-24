from django.shortcuts import render, redirect

from clients.models import Client
from health_fitness_tests.forms import BodyMassForm, BodyHeightForm

# Create your views here.

def test_client_list(request):
    client_list = Client.objects.filter(user=request.user)
    return render(request, 'health_fitness_tests/health_fitness_client_list.html', {'client_list': client_list})

def client_dashboard(request, pk):
    client = Client.objects.get(pk=pk)

    context = {
        'client': client
    }

    return render(request, 'health_fitness_tests/client_dashboard.html', context)

def update_add(request, pk):
    client = Client.objects.get(pk=pk)
    form = BodyHeightForm()
    weight = BodyMassForm()



    if request.method == 'POST':
        height_form = BodyHeightForm(request.POST)
        mass_form = BodyMassForm(request.POST)

        if height_form.is_valid():
            height = height_form.save(commit=False)
            height.client = client
            height.save()

        if mass_form.is_valid():
            mass = mass_form.save(commit=False)
            mass.client = client
            mass.save()

            return redirect('health_fitness_tests:client_dashboard_url', pk=client.pk)


    context = {
        'client': client,
        'form': form,
        'weight': weight,
    }

    return render(request, 'health_fitness_tests/update_add.html', context)
