from django import forms
from .models import JournalEntry

# Lab 4: Creating the Form for user input
class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        # We handle 'author' in the view, so it's not in the form (Lab 6)
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Entry Title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your thoughts here...'}),
        }