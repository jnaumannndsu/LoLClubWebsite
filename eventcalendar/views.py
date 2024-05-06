from datetime import datetime
from django.shortcuts import render
from eventcalendar.models import Event, Game, Lan, Tournament, Hof, Result
from django.views import generic
from django.urls import reverse_lazy


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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.object
        dataList = [event]
        #Create list of games, lans, tournaments with same id
        games = Game.objects.filter(event = event.eventID)
        lans = Lan.objects.filter(event = event.eventID)
        tournaments = Tournament.objects.filter(event = event.eventID)
        #If to add specific event type to dataList
        if games:
            dataList.append(games[0])
        elif lans:
            dataList.append(lans[0])
        elif tournaments:
            dataList.append(tournaments[0])
        #Create and return context
        context = {'list' : dataList}
        return context

class ResultDetailView(generic.DetailView):
    model = Result

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

class EventCreate(PermissionRequiredMixin,CreateView):
    model = Event
    fields = ['eventID', 'startTime', 'endTime', 'eventName']
    permission_required = 'eventcalendar.add_event'

class EventUpdate(PermissionRequiredMixin,UpdateView):
    model = Event
    fields = '__all__'
    permission_required = 'eventcalendar.change_event'

class EventDelete(PermissionRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('calendar')
    permission_required = 'eventcalendar.delete_event'

class ResultCreate(PermissionRequiredMixin, CreateView):
    model = Result
    fields = ['name', 'date', 'score', 'division']
    permission_required = 'eventcalendar.add_result'

class ResultUpdate(PermissionRequiredMixin, UpdateView):
    model = Result
    fields = '__all__'
    permission_required = 'eventcalendar.change_result'

class ResultDelete(PermissionRequiredMixin, DeleteView):
    model = Result
    success_url = reverse_lazy('results')
    permission_required = 'eventcalendar.delete_result'
