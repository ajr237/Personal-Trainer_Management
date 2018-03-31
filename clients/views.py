from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>PT Manager Homepage</h1>')

def index2(request):
    return render(request, 'index.html', {})
