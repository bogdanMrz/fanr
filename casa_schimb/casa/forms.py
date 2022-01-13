from django import forms
from .models import *


from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class DateInput(forms.DateInput):
    input_type = 'date'



class TimeInput(forms.DateTimeInput):
    input_type = 'time'


class Calendar(forms.Form):
    calendar = DateField(widget=DateInput)


class CreateClient1Form(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['tara']

        widgets = {
            'data_nasterii' : DateInput(),
            'adresa' : forms.Textarea,
            'numar_document' : forms.TextInput(attrs={'class': 'special'})
        }




class CreateClient2Form(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['adresa']

        widgets = {
            'data_nasterii' : DateInput(),
            'numar_document' : forms.TextInput(attrs={'class': 'special'})

            }



class CreateValutaForm(forms.ModelForm):
    class Meta:
        model = Valuta
        exclude = []

        widgets = {}


class EditValutaForm(forms.ModelForm):
    class Meta:
        model = Valuta
        exclude = []
        widgets = {'sold' : forms.HiddenInput}


class Soldform(forms.Form):
    sold = forms.FloatField(disabled = True)    


class CreateCotatieForm(forms.ModelForm):
    class Meta:
        model = Cotatie
        exclude = []

        widgets = {
            'data' : DateInput(),
            'ora' : TimeInput()
        
        }


class CreateBuletinDeSchimbForm(forms.ModelForm):
    class Meta:
        model = BuletinDeSchimb
        exclude = []

        #widgets = {'data' : forms.DateTimeInput(attrs={'type': 'date'})}
        widgets = {
            'data' : DateInput(),
            'ora' : TimeInput()

            }
