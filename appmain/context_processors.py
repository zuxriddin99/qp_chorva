from django.shortcuts import render
from constance import config
from .models import Menu


def myview(request):
    menu = Menu.objects.all()
    context = {'config': config,
               'menu': menu}
    return context
