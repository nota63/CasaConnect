from .models import HelpMod
from django import forms


# help form

class HelpForm(forms.ModelForm):
    class Meta():
        model = HelpMod
        fields = ['email', 'contact','keywords']
