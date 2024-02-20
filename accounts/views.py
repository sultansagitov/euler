from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.core.handlers.wsgi import WSGIRequest
from django.core.exceptions import ObjectDoesNotExist

from .forms import RegisterForm
from .models import Student, FriendRequest

import json
import base64
import io
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


def register(request: WSGIRequest):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)

            student, _ = Student.objects.get_or_create(user=user)

            if request.POST["data_avatar"]:
                data = base64.b64decode(request.POST["data_avatar"].split(";base64,")[-1].encode('UTF-8'))
                buf = io.BytesIO(data)
                img = Image.open(buf)

                content_type = request.POST["data_avatar"].split(";base64,")[0][5:]

                img_io = io.BytesIO()
                img.save(img_io, format=content_type.split("/")[1].upper())
                student.avatar = InMemoryUploadedFile(img_io,
                                                      field_name=None,
                                                      name=f"{student.pk}.{content_type.split('/')[-1]}",
                                                      content_type=content_type,
                                                      size=img_io.tell,
                                                      charset=None)

                student.save()

            return redirect(reverse('levels'))
        else:
            return render(request, 'registration/register.html', {'form': form})

    return render(request, 'registration/register.html', {})


def logout_view(request: WSGIRequest):
    if request.user.is_authenticated:
        logout(request)

    return redirect(reverse('index'))


@login_required
def profile(request: WSGIRequest):
    return render(request, 'profile.html')


@login_required
def editprofile(request: WSGIRequest):
    if request.method != "POST":
        return render(request, 'editprofile.html')
    else:
        request.user.username = request.POST.get("username")
        request.user.save()

        request.user.student.country = request.POST.get("country")
        request.user.student.city = request.POST.get("city")
        request.user.student.bio = request.POST.get("bio")
        request.user.student.save()

        return redirect(reverse("profile"))


@login_required
def friends(request):
    res = render(request, "friends.html", {
        "friends": request.user.student.friends.all(),
        "notfriends":
        Student.objects
            .exclude(user=request.user)
            .exclude(friends=request.user.student)
            .exclude(friendrequests_to__touser=request.user.student).all(),
        "friendrequests": request.user.student.friendrequests_from.all(),
    })

    for notification in request.user.student.friendnotification_from.iterator():
        notification.delete()

    return res
