from django import forms
from django.forms.extras.widgets import SelectDateWidget
from events.models import Event, Player


class EventForm(forms.ModelForm):
    """
    Form for creating a new event.
    """
    class Meta:
        model = Event
        exclude = ['creator',
                   'created_date',
                   'modified_date',
                   'published_date',
                   'players',
                   ]
        widgets = {
            'date': SelectDateWidget(),
        }


class SignUpForm(forms.Form):
    """
    Form that players can use to sign up for a game.
    """
    class Meta:
        model = Player
        exclude = ['participating_in',
                   ]
        widgets = {
            'birthday': SelectDateWidget(),
        }


class ContactForm(forms.Form):
    """
    Form for contacting the creator of an event.
    Currently unused. Included because this will be added in the future.
    """
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)