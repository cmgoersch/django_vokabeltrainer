from django import forms
from .models import Wort

class WortForm(forms.ModelForm):
    class Meta:
        model = Wort
        fields = ['deutsch', 'finnisch', 'kategorie']