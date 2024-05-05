from django.contrib import admin
from django.urls import path, include
from statsviewer import views


urlpatterns = [
    path('stats_home', views.stats, name = 'stats-home'),
]