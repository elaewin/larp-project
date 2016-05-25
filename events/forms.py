from django import forms
from django.forms.extras.widgets import SelectDateWidget
from events.models import Event


class EventForm(forms.ModelForm):
    """
    Form for creating a new event.
    """
    class Meta:
        model = Event
        exclude = ['creator',
                   'created_date',
                   'modified_date',
                   'published_date'
                   ]
        widgets = {
            'date': SelectDateWidget(),
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