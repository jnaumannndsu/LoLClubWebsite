from django.urls import path, include
from eventcalendar import views

urlpatterns = [
    path('', views.home, name="home"  ),
    path('calendar/', views.calendar, name = "calendar"),
    path('results/', views.results, name = 'results'),
    path('rosters/', views.rosters, name = 'rosters'),
    path('officers/', views.officers, name = 'officers'),
    path('minutes/', views.minutes, name = 'minutes'),
    path('hof/', views.hof, name = 'hof'),
    #me trying to make event detail view 
    path('calendar/<int:pk>', views.eventDetailView.as_view(), name = 'event-detail'),
    path('stats/', include('statsviewer.urls')),
    path('calendar/create/', views.EventCreate.as_view(), name = 'event-create')
]

