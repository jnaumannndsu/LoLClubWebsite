from django.contrib import admin
from django.urls import path, include
from statsviewer import views



urlpatterns = [
    path('stats_home', views.stats, name = 'stats-home'),
    path('stats_home/player_list/', views.playerListView, name = 'player-list'),
    path('stats_home/player/<int:pk>', views.playerDetailView.as_view(), name = 'player-detail'),
    path('stats_home/game_list/', views.gameListView, name = 'game-list'),
    path('stats_home/game/<int:pk>', views.gameDetailView.as_view(), name = 'game-detail'),

    path('', views.gohome, name = 'go-home'),
]

