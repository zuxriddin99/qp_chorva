from django.shortcuts import render
from constance import config
from .models import Menu


def myview(request):
    menus = Menu.objects.all()
    context = {'config': config,
               'menus': menus}
    return context
