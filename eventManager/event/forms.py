from django import forms
from .models import Event, Registration

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'location', 'max_participants']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []
