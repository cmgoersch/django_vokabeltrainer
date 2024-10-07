from django import forms
from .models import Wort, Satz

class WortForm(forms.ModelForm):
    class Meta:
        model = Wort
        fields = ['deutsch', 'finnisch', 'merksatz']  # Kategorie wird nicht mehr angezeigt

class SatzForm(forms.ModelForm):
    class Meta:
        model = Satz
        fields = ['deutsch', 'finnisch', 'merksatz']  # Kategorie wird nicht mehr angezeigt