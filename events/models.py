from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    '''
    Class for creating new game events.
    '''
    title = models.CharField(max_length=128)
    creator = models.ForeignKey(User)
    game_system = models.CharField(max_length=128)
    online_rules = models.BooleanField(default=False)
    rules_url = models.URLField(blank=True)
    # date = models.DateTimeField(blank=True)
    # checkin = models.TimeField(blank=True)
    # game_on = models.TimeField(blank=True)
    # game_off = models.TimeField(blank=True)
    location_address1 = models.CharField(max_length=64, blank=True)
    location_address2 = models.CharField(max_length=64, blank=True)
    location_city = models.CharField(max_length=64, blank=True)
    location_state = models.CharField(max_length=2, blank=True)
    contact_name = models.CharField(max_length=128, blank=True)
    contact_email = models.EmailField(blank=True)
    pregens = models.BooleanField(default=False)
    age_restriction = models.BooleanField(default=True)
    age_limit = models.PositiveSmallIntegerField(default="18")
    cost = models.PositiveSmallIntegerField(default="0")

    def __str__(self):
        return self.title
