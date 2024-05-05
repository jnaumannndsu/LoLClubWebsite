from django.shortcuts import render
from django.views import generic
from statsviewer.models import *

# Create your views here.
def stats(request):
    return render(request, 'stats_home.html')

def playerListView(request):
    allPlayers = Player.objects.all()
    playerList = []
    for p in allPlayers:
        #kills deaths assists gold dmg
        dataList = [p,0,0,0,0,0]
        instances = PlayerInstance.objects.filter(player = p.playerid)
        #swag method
        for pi in instances:
            dataList[1] += pi.kills
            dataList[2] += pi.deaths
            dataList[3] += pi.assists
            dataList[4] += pi.gold
            dataList[5] += pi.damage
        playerList.append(dataList)
    
    return render(request, 'player_list.html', {'list' : playerList})
            

        
            

class playerDetailView(generic.DetailView):
    model = Player

class gameListView(generic.ListView):
    model = Game

class gameDetailView(generic.DetailView):
    model = Game