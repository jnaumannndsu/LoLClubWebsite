from django.shortcuts import get_object_or_404, redirect, render
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
            
def gohome(request):
    return redirect(reverse('home', current_app='eventcalendar'))
        
            
# PLAYER DETAIL VIEW WE WANT TO HAVE
# PLAYER STATS FROM BEFORE (PIS)
# GAMES WIN LOSS TOTAL

class playerDetailView(generic.DetailView):
    model = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player = self.object
        dataList = [player,0,0,0,0,0,0,0]
        instances = PlayerInstance.objects.filter(player = player.playerid)
        #swag method
        for pi in instances:
            game = Game.objects.filter(pk = pi.game.gameid)  
            if pi.playerlocation <= 4 and game[0].winner == True or pi.playerlocation > 4 and game[0].winner == False:
                dataList[6] += 1
            else:
                dataList[7] += 1
            dataList[1] += pi.kills
            dataList[2] += pi.deaths
            dataList[3] += pi.assists
            dataList[4] += pi.gold
            dataList[5] += pi.damage
        context = {'list' : dataList}
        return context

class gameListView(generic.ListView):
    model = Game

class gameDetailView(generic.DetailView):
    model = Game