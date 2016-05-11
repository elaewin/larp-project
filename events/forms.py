from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = (
            'title',
            'title',
            'game_system',
            'online_rules',
            'rules_url',
            'description',
            'date',
            'checkin',
            'game_on',
            'game_off',
            'location_address1',
            'location_address2',
            'location_city',
            'location_state',
            'location_zip',
            'contact_name',
            'contact_email',
            'pregens',
            'character_info',
            'age_restriction',
            'age_limit',
            'cost',
            )


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)