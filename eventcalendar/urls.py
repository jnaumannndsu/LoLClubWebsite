from django.urls import path, include
from eventcalendar import views

urlpatterns = [
    path('', views.home, name="home"  )
    path('calendar/', views.c)
]