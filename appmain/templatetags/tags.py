from django import template
from constance import config

register = template.Library()


@register.filter
def even(id):
    if id % 2 == 0 or id == 0:
        return True

    return False


@register.filter
def translate(name, url):
    return config.__getattr__(name + url.split('/')[1])
