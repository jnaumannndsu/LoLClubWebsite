from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.
class Game(models.Model):
    gameid = models.BigAutoField(primary_key=True)
    winner = models.BooleanField(null=False)

    def __str__(self):
        if self.winner == True:
            return "Blue | ID: " + str(self.gameid)
        return "Red | ID: " + str(self.gameid)
    def get_absolute_url(self):
        return reverse("game-detail", args=[str(self.gameid)])


class PlayerInstance(models.Model):
    instanceid = models.BigAutoField(primary_key=True)
    game = models.ForeignKey('Game', on_delete=models.RESTRICT)
    playerlocation = models.IntegerField(null=False, validators=[MaxValueValidator(9), MinValueValidator(0)])
    ROLE_FIELDS = (
        ('t', 'TOP'),
        ('j', 'JUNGLE'),
        ('m', 'MID'),
        ('a', 'ADC'),
        ('s', 'SUP'),
    )
    role = models.CharField(max_length=1, choices=ROLE_FIELDS, help_text='What role did they play')
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    gold = models.IntegerField()
    damage = models.IntegerField()
    ign = models.CharField(max_length=30)
    player = models.ForeignKey('Player', on_delete=models.RESTRICT)

    def __str__(self):
        return self.ign + "--" + str(self.instanceid)
    def get_absolute_url(self):
        return reverse("game-detail", args=[str(self.instanceid)])

class Player(models.Model):
    class Meta:
        unique_together = (('playerid','name'),)
    playerid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("player-detail", args=[str(self.playerid)])
    
