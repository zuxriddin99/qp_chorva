from django.views.generic import ListView

from django.shortcuts import render
from .models import *


# Create your views here.

class AboutCompanyView(ListView):
    queryset = AboutCompany.objects.filter(show=True)
    template_name = 'about.html'
