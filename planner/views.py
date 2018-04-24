from django.shortcuts import render

# Create your views here.
def calendar(request):
    return render(request, 'planner/calendar.html', {})

def calendar_by_period(request, calendar_slug='training-sessions'):
    return render(request, 'schedule/calendar_by_period.html', {})
