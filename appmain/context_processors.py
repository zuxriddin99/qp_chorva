from django.shortcuts import render
from constance import config


def myview(request):
    context = {'config': config}
    return context
