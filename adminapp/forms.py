from django import forms
from userapp.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_type']
