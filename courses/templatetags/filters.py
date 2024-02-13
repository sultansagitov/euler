import random
from django import template

from django.contrib.auth.models import User 
from courses.models import Question


register = template.Library()


@register.filter
def answered(question: Question, user: User):
    return question.answered(user)
