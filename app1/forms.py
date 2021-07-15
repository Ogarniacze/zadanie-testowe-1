from django import forms
from django.forms import ModelForm
from .models import City


class CityForm(ModelForm):
    city = forms.CharField(label='Nazwa miasta', max_length=100, required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'disabled': False,
                                   'class': 'form-control',
                                   'placeholder': 'Nazwa miasta', }))
    citizens = forms.CharField(label='Ilość mieszkańców', max_length=20, required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       'disabled': False,
                                       'class': 'form-control',
                                       'placeholder': 'Ilość mieszkańców', }))

    class Meta:
        model = City
        fields = ['city', 'citizens', ]
