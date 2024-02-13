import random
from django import template


register = template.Library()


@register.filter
def shuffle(arg):
    temp = list(arg)[:]
    random.shuffle(temp)
    return temp


@register.filter
def enum(arg):
    return enumerate(arg)