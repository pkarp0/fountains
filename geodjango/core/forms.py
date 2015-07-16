#coding: utf-8
from django.contrib.gis import forms
from geodjango.core.models import Land

class LandForm(forms.ModelForm):
    class Meta:
        model = Land       
        fields = ['area',]
