from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.handlers.wsgi import WSGIRequest


def index(request: WSGIRequest):
    if request.user.is_authenticated:
        return redirect(reverse('levels'))
    else:
        return render(request, 'mainpage.html')
