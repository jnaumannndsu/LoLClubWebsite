from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    eventID = models.BigAutoField(primary_key=True)
    startTime = models.DateTimeField(blank=True)
    endTime = models.DateTimeField()
    eventName = models.CharField(default="New Event", max_length=160)
    
    def __str__(self):
        return self.eventName
    
    def get_absolute_url(self):
        return reverse("event-detail", args=[str(self.eventID)])
    



class Lan(models.Model):
    event = models.OneToOneField('Event', on_delete=models.CASCADE, null=False, primary_key=True)
    location = models.CharField(max_length=320)

class Tournament(models.Model):
    event = models.OneToOneField('Event', on_delete=models.CASCADE, null=False, primary_key=True)
    STREAM_STATUS = (
        ('m', 'Main'),
        ('a', 'Alt'),
        ('n', 'None'),
    )
    status = models.CharField(max_length=1, choices=STREAM_STATUS, blank=True, default='n', help_text='Where streamed')
    signup = models.URLField()

class Game(models.Model):
    event = models.OneToOneField('Event', on_delete=models.CASCADE, null=False, primary_key=True)
    TEAM_FIELDS = (
        ('v', 'Varsity'),
        ('j', 'Junior Varsity'),
        ('c', 'C Team'),
        ('d', 'D Team'),
        ('o', 'Other'),
    )
    team = models.CharField(max_length=1, choices = TEAM_FIELDS, blank=True, help_text= 'Team playing')
    LEAGUE_FIELDS = (
        ('c', 'CCL'),
        ('n', 'NECC'),
        ('e', 'NACE'),
        ('o', 'Other'),
    )
    league = models.CharField(max_length=1, choices=LEAGUE_FIELDS, blank=True, help_text='What League are they competing in')
    STREAM_STATUS = (
        ('m', 'Main'),
        ('a', 'Alt'),
        ('n', 'None'),
    )
    status = models.CharField(max_length=1, choices=STREAM_STATUS, blank=True, default='n', help_text='Where streamed')

class Result(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    score = models.CharField(max_length=5)
    division = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse("result-detail", kwargs={"pk": self.pk})
    
    
class Hof(models.Model):
    tourneyName = models.CharField(max_length=30)
    teamName = models.CharField(max_length=30)
    player1 = models.CharField(max_length=30)
    player2 = models.CharField(max_length=30)
    player3 = models.CharField(max_length=30)
    player4 = models.CharField(max_length=30)
    player5 = models.CharField(max_length=30)

    def __str__(self):
        return self.tourneyName
