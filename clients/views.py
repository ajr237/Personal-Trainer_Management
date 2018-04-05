from django.shortcuts import render, HttpResponse

# def index2(request):
#     return render(request, 'index.html', {})

def dashboard(request):
    return render(request, 'clients/index.html', {})
