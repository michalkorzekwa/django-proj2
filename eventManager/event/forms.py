from django import forms
from .models import Event, Registration

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'location', 'max_participants']
        
        date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local', 
        })
    )
        widgets = {
            'date': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []


from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
