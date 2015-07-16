#coding: utf-8
from django.shortcuts import render
from geodjango.core.forms import LandForm
from geodjango.core.models import Place

def home(request):
    return render(request, 'index.html', { 'form': LandForm(), 'points': Place.objects.all() })
