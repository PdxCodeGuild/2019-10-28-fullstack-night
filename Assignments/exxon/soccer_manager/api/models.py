from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Player(models.Model):
    name = models.CharField(max_length=60)
    position = models.CharField(max_length=60)

    def __str__(self):
        return (self.name + ' - ' + self.position)


class PlayerPhoto(models.Model):

# definition of positions that show up when rendered on html the def in " " shows up on page

    GOALKEEPER = 'Goalkeeper'
    RIGHT_FULLBACK = 'Right-Fullback'
    LEFT_FULLBACK = 'Left-Fullback'
    CENTER_BACK = 'Center-Back'
    SWEEPER = 'Sweeper'
    DEFENDING_HOLDING_MIDFIELDER = "Defending-Midfielder"
    RIGHT_MIDFIELDER = 'Right-Midfielder'
    CENTER_MIDFIELDER = 'Center-Midfielder'
    STRIKER = 'Striker'
    ATTACKING_MIDFIELDER = 'Attacking-Midfielder'
    LEFT_MIDFIELDER = 'Left-Midfielder'


    PLAYER_POSITIONS = (
        (GOALKEEPER , 'Goalkeeper'),
        (RIGHT_FULLBACK, 'Right-Fullback'),
        (LEFT_FULLBACK, 'Left-Fullback'),
        (CENTER_BACK, 'Center-Back'),
        (SWEEPER, 'Sweeper'),
        (DEFENDING_HOLDING_MIDFIELDER, 'Defending-Midfielder'),
        (RIGHT_MIDFIELDER, 'Right-Midfielder'),
        (CENTER_MIDFIELDER, 'Center-Midfielder'),
        (STRIKER, 'Striker'),
        (ATTACKING_MIDFIELDER, 'Attacking-Midfielder'),
        (LEFT_MIDFIELDER, 'Left-Midfielder')
    )





    position = models.CharField(max_length=30, choices=PLAYER_POSITIONS, blank=True)
    name = models.CharField(max_length=255, blank=True)
    number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='photos', max_length=300, blank=True)
    starter = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User',default=None,blank=True, on_delete=models.CASCADE)


    def __unicode__(self):
        return self.name



    def __repr__(self):
        return self.__str__()