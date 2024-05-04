from django.shortcuts import render
from eventcalendar.models import Event, Game, Lan, Tournament

# Create your views here.
def home(request):
    return render(request, 'home.html')

def calendar(request):
    return render(request, 'calendar.html')

def results(request):
    return render(request, 'results.html')

def rosters(request):
    return render(request, 'rosters.html')

def officers(request):
    return render(request, 'offciers.html')

def minutes(request):
    return render(request, 'minutes.html')

def hof(request):
    return render(request, 'hof.html')