from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def admin_required(func):
    @login_required
    def res(request: WSGIRequest):
        if request.user.student.admin:
            return func(request)
        else:
            return render(request, "messages/donthaverights.html", status=400)

    return res
