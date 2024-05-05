from datetime import datetime
from django.shortcuts import render
from eventcalendar.models import Event, Game, Lan, Tournament, Hof, Result
from django.views import generic


# Create your views here.
def home(request):
    return render(request, 'home.html')

def calendar(request):
    # PASS LIST OF EVENTS THAT HAVE NOT HAPPENED

    current_datetime = datetime.now()
    events = Event.objects.filter(endTime__gte = current_datetime)
    return render(request, 'calendar.html', {'events' : events})

def results(request):
    results = Result.objects.all()
    return render(request, 'results.html', {'results' : results})

def rosters(request):
    return render(request, 'rosters.html')

def officers(request):
    return render(request, 'officers.html')

def minutes(request):
    return render(request, 'minutes.html')

def hof(request):
    hofs = Hof.objects.all()
    return render(request, 'hof.html', {'hofs' : hofs})


class eventDetailView(generic.DetailView):
    model = Event
