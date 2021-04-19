from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('long_url', 'short_url', 'user')

        labels = {
            'long_url': '',
            'short_url': ''
        }

        widgets = {
            'long_url': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: 20px;', 'placeholder': 'Enter your URL here...'})
        }