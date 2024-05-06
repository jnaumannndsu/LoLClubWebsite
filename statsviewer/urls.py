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
    path('stats_home/game_list/create/', views.GameCreate.as_view(), name = 'game-create'),
    path('stats_home/game/<int:pk>/update', views.GameUpdate.as_view(), name = 'game-update'),
    path('stats_home/game/<int:pk>/delete', views.GameDelete.as_view(), name = 'game-delete'),
    path('stats_home/player_list/create/', views.PlayerCreate.as_view(), name = 'player-create'),
    path('stats_home/player/<int:pk>/update', views.PlayerUpdate.as_view(), name = 'player-update'),
    path('stats_home/player/<int:pk>/delete', views.PlayerDelete.as_view(), name = 'player-delete'),
    path('stats_home/player_list/instance/create/', views.PlayerInstanceCreate.as_view(), name = 'instance-create'),
    path('stats_home/player/instance/<int:pk>/update', views.PlayerInstanceUpdate.as_view(), name = 'instance-update'),
    path('stats_home/player/instance/<int:pk>/delete', views.PlayerInstanceDelete.as_view(), name = 'instance-delete'),
    path('stats_home/player/instance/<int:pk>/', views.PlayerInstanceDetailView.as_view(), name = 'instance-detail'),
]

