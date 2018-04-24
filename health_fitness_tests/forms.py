from django import forms
from .models import BodyHeight, BodyMass

class BodyHeightForm(forms.ModelForm):

    height = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Body Height (m)'}))

    class Meta():
        model = BodyHeight
        fields = (
            'height',
            )

class BodyMassForm(forms.ModelForm):

    class Meta():
        model = BodyMass
        fields = (
            'mass',
            )
