from django.shortcuts import render
from eventcalendar.models import Event, Game, Lan, Tournament

# Create your views here.
def home(request):
    return render(request, 'home.html')

def calendar(request):
    return render(request, 'calendar.html')