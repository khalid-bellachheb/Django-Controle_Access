from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView

from .models import data_ttn



class Data_ListView(ListView):
    model = data_ttn
