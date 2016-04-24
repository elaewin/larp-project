from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    '''
    Class for creating new game events.
    '''
    title = models.CharField(max_length=128)
    creator = models.ForeignKey(User)
    game_system = models.CharField(max_length=128)
    online_rules = models.BooleanField()
    # rules_url = models.URLField(blank=True)
    # date = models.DateTimeField()
    # checkin = models.TimeField()
    # game_on = models.TimeField()
    # game_off = models.TimeField()
    # location_address1 = models.CharField(max_length=64)
    # location_address2 = models.CharField(max_length=64, blank=True)
    # location_city = models.CharField(max_length=64)
    # location_state = models.CharField(max_length=2)
    # contact_name = models.CharField(max_length=128)
    # contact_email = models.EmailField()
    # pregens = models.BooleanField()
    # age_restriction = models.BooleanField()
    # age_limit = models.PositiveSmallIntegerField()
    # cost = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title
