from django import forms
from django.utils import timezone
from django.core import validators

from .models import Client
YEARS = []
for i in range(1930,timezone.now().year+1):
    YEARS.append(i)


class ClientForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),validators=[validators.validate_email])
    contact_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}))
    gender = forms.ChoiceField(choices=Client.GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    date_of_birth = forms.DateField(initial="1990-06-21", widget=forms.SelectDateWidget(years=YEARS, attrs={'class': 'form-control form-control-sm'}))
    class Meta():
        model = Client
        fields = (
            'first_name',
            'last_name',
            'gender',
            'date_of_birth',
            'email',
            'contact_number'
            )
    # def clean_date_of_birth(self):
    #     data = self.cleaned_data['date_of_birth']
    #     if "-" not in data:
    #         raise forms.ValidationError("Please state DOB in yyyy-mm-yy format")
    #
    #     # Always return a value to use as the new cleaned data, even if
    #     # this method didn't change it.
    #     return data
