from django import template

register = template.Library()


@register.filter
def even(id):
    if id % 2 == 0 or id != 0:
        return True

    return False
