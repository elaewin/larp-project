from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class Player(models.Model):
    """
    """
    name = models.ForeignKey(User)
    participating_in = models.ManyToManyField('self', through='Participation',
                                        symmetrical=False,
                                        related_name='playing_in')

    def __str__(self):
        return str(self.name)


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
    players = models.ManyToManyField(Player, through='Participation')

    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Events'


PARTICIPATION_PLAYING = 1
PARTICIPATION_NOT_PLAYER = 2
PARTICIPATION_STATUSES = (
    (PARTICIPATION_PLAYING, 'Playing'),
    (PARTICIPATION_NOT_PLAYER, 'Not Playing'),
    )


class Participation(models.Model):
    """
    """
    person = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.IntegerField(choices=PARTICIPATION_STATUSES)

    def __str__(self):
        return self.game.title

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

