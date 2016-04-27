from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    """
    Class for all game events.
    """
    title = models.CharField("Game Title", max_length=128)
    creator = models.ForeignKey(User)
    game_system = models.CharField(max_length=128)
    online_rules = models.BooleanField("Rules set is online", default=False)
    rules_url = models.URLField("Rules URL", blank=True)
    description = models.TextField(blank=True)
    date = models.DateField("Game Date", blank=True, default="2016-01-01")
    checkin = models.TimeField("Check-in opens", blank=True, default="12:00:00.000")
    game_on = models.TimeField("Game on at", blank=True, default="12:00:00.000")
    game_off = models.TimeField("Game off at", blank=True, default="12:00:00.000")
    location_address1 = models.CharField("Game location address", max_length=64, blank=True)
    location_address2 = models.CharField("Address, cont.", max_length=64, blank=True)
    location_city = models.CharField("City", max_length=64, blank=True)
    location_state = models.CharField("State", max_length=2, blank=True)
    contact_name = models.CharField("Organizer contact name", max_length=128, blank=True)
    contact_email = models.EmailField("Organizer email address", blank=True)
    pregens = models.BooleanField("Game uses pregenerated characters", default=False)
    age_restriction = models.BooleanField("Game is restricted by age", default=True)
    age_limit = models.PositiveSmallIntegerField("Minimum age to play", default="18")
    cost = models.PositiveSmallIntegerField("Game cost/Site fee", default="0")

    def __str__(self):
        return self.title
