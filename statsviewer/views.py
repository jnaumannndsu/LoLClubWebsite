from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from statsviewer.models import  *
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def stats(request):
    total_damage = 0
    total_gold = 0
    total_deaths = 0
    num_players = Player.objects.all().count
    num_games = Game.objects.all().count
    for p in PlayerInstance.objects.all():
        total_damage += p.damage
        total_deaths += p.deaths
        total_gold += p.gold

    context = {
        'num_players': num_players,
        'num_games' : num_games,
        'damage' : total_damage,
        'deaths' : total_deaths,
        'gold' : total_gold,
    }

    return render(request, 'stats_home.html', context=context)

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
        #player, kils, deaths, assists, gold, damage, wins, losses
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
    

def gameListView(request):
    allGames = Game.objects.all()
    gameList = []
    for g in allGames:
        dataList = [g]
        playerInstances = PlayerInstance.objects.filter(game = g.pk)
        for p in playerInstances:
            dataList.append(p)
        gameList.append(dataList)
        

    return render(request, 'game_list.html', {'list' : gameList})

class gameDetailView(generic.DetailView):
    model = Game

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = self.object
        dataList = [game]
        playerInstances = PlayerInstance.objects.filter(game = game.pk)
        for p in playerInstances:
            dataList.append(p)
        context = {'list' : dataList}
        return context

from django.contrib.auth.mixins import PermissionRequiredMixin

class GameCreate(PermissionRequiredMixin, CreateView):
    model = Game
    fields = ['winner']
    permission_required = 'statsviewer.add_game'

class GameUpdate(PermissionRequiredMixin, UpdateView):
    model = Game
    fields = '__all__'
    permission_required = 'statsviewer.update_game'

class GameDelete(PermissionRequiredMixin, DeleteView):
    model = Game
    success_url = reverse_lazy('game_list')
    permission_required = 'statsviewer.delete_game'

class PlayerCreate(PermissionRequiredMixin, CreateView):
    model = Player
    fields = ['name']
    permission_required = 'statsviewer.add_player'

class PlayerUpdate(PermissionRequiredMixin, UpdateView):
    model = Player
    fields = '__all__'
    permission_required = 'statsviewer.update_player'

class PlayerDelete(PermissionRequiredMixin, DeleteView):
    model = Player
    success_url = reverse_lazy('player_list')
    permission_required = 'statsviewer.delete_player'

class PlayerInstanceCreate(PermissionRequiredMixin, CreateView):
    model = PlayerInstance
    fields = ['game', 'playerlocation', 'role', 'kills', 'deaths', 'assists', 'gold', 'damage', 'ign', 'player']
    permission_required = 'statsviewer.add_playerinstance'

class PlayerInstanceUpdate(PermissionRequiredMixin, CreateView):
    model = PlayerInstance
    fields = '__all__'
    permission_requierd = 'stasviewer.update_playerinstance'
    
class PlayerInstanceDelete(PermissionRequiredMixin, DeleteView):
    model = PlayerInstance
    success_url = reverse_lazy('player_list')
    permission_required = 'statsviewer.delete_playerinstance'