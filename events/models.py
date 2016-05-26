from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class Event(models.Model):
    """
    Class for all game events.
    """
    title = models.CharField("Game Title", max_length=128)
    creator = models.ForeignKey(User)
    game_system = models.CharField(max_length=128)
    online_rules = models.BooleanField("Rules set is online", default=False)
    rules_url = models.URLField("Rules URL", blank=True)
    description = RichTextField(blank=True)
    date = models.DateField("Game Date", blank=True, default="2016-01-01")
    checkin = models.TimeField("Check-in opens", blank=True, default="12:00")
    game_on = models.TimeField("Game on at", blank=True, default="12:00")
    game_off = models.TimeField("Game off at", blank=True, default="12:00")
    location_address1 = models.CharField("Game location address", max_length=64, blank=True)
    location_address2 = models.CharField("Address, cont.", max_length=64, blank=True)
    location_city = models.CharField("City", max_length=64, blank=True)
    location_state = models.CharField("State", max_length=2, blank=True)
    location_zip = models.CharField("Zip/Postal Code", max_length=24, blank=True)
    contact_name = models.CharField("Organizer contact name", max_length=128, blank=True)
    contact_email = models.EmailField("Organizer email address", blank=True)
    pregens = models.BooleanField("Game uses pregenerated characters", default=False)
    character_info = RichTextField("Character Creation Info", blank=True)
    age_restriction = models.BooleanField("Game is restricted by age", default=True)
    age_limit = models.PositiveSmallIntegerField("Minimum age to play", default="18")
    cost = models.PositiveSmallIntegerField("Game cost/Site fee", default="0")
    created_date = models.DateTimeField("Created", auto_now_add=True)
    modified_date = models.DateTimeField("Modified", auto_now=True)
    published_date = models.DateTimeField("Published", blank=True, null=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Events'


# class Tag(models.Model):
#     """
#     Class for adding content tags to games.
#     """
#     name = models.CharField(max_length=128)
#     description = models.TextField(blank=True)
#     events = models.ManyToManyField(Event, blank=True, related_name='tags')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = 'Tags'


class Participant(models.Model):
    """
    Lists of participants for each game.
    """
    game = models.ForeignKey(Event)
    players = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.game.title

    class Meta:
        verbose_name_plural = 'Participants'
